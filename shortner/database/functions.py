from datetime import datetime, timezone

from cassandra.cluster import Session


def get_long_url(session: Session, short_url: str) -> str | None:
    query = 'select long_url from urls where shortcode = %s'

    result = session.execute(query, (short_url,)).one()

    if result is None:
        return None

    return result.long_url


def register_new_url(session: Session, short_url: str, long_url: str) -> None:
    query = (
        'insert into shortner.urls (shortcode, created_at, long_url) '
        'values (%s, %s, %s)'
    )
    session.execute(query, (short_url, datetime.now(timezone.utc), long_url))
