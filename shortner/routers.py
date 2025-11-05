from http import HTTPStatus
from typing import Annotated

from cassandra.cluster import Session
from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from starlette.responses import RedirectResponse

import shortner.cache.functions as cache
import shortner.cache.session as cache_session
import shortner.counter.functions as counter
import shortner.counter.session as counter_session
import shortner.database.functions as database
import shortner.database.session as database_session
from shortner.exceptions.url_exceptions import HostException, ProtocolException
from shortner.schemas import ServerStatus, UrlSchema, UrlShortenCreated
from shortner.security import url_encoder
from shortner.settings import Settings
from shortner.validation.url import URL

router = APIRouter(tags=['URL Shortner'])

settings = Settings()

T_Cassandra = Annotated[Session, Depends(database_session.get_session)]
T_RedisCounter = Annotated[Redis, Depends(counter_session.get_session)]
T_Redis_cache = Annotated[Redis, Depends(cache_session.get_session)]


@router.post(
    '/shorten',
    status_code=HTTPStatus.CREATED,
    response_model=UrlShortenCreated,
)
def shorten_url(
    long_url: UrlSchema,
    redis_counter_session: T_RedisCounter,
    cassandra_session: T_Cassandra,
    redis_cache_session: T_Redis_cache,
):
    try:
        validated_url = URL(long_url.url)

    except (HostException, ProtocolException) as ex:
        raise HTTPException(HTTPStatus.BAD_REQUEST, ex.args)

    url_as_int = counter.increment_counter(redis_counter_session)

    encoded_url = url_encoder.encode(url_as_int)

    database.register_new_url(
        cassandra_session, encoded_url, validated_url.long_url
    )

    cache.set_value_in_cache(
        redis_cache_session, encoded_url, validated_url.long_url
    )

    return {'short_url': f'{settings.APP_ENDPOINT}{encoded_url}'}


@router.get('/status', status_code=HTTPStatus.OK, response_model=ServerStatus)
def get_server_status():
    return {'status': 'Ok'}


@router.get('/{short_url}')
def access_endpoint(
    short_url: str,
    cassandra_session: T_Cassandra,
    redis_cache_session: T_Redis_cache,
):
    if cache.check_if_key_in_cache(redis_cache_session, short_url):
        long_url = cache.get_key_value_in_cache(redis_cache_session, short_url)

    else:
        long_url = database.get_long_url(cassandra_session, short_url)

    if long_url is None:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail='Address not found.')

    return RedirectResponse(long_url, status_code=HTTPStatus.FOUND)
