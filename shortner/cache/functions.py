from rediscluster import RedisCluster


def check_if_key_in_cache(cache_session: RedisCluster, key: str) -> bool:
    response = cache_session.exists(key)

    return True if response == 1 else False


def get_key_value_in_cache(cache_session: RedisCluster, key: str) -> str:
    response: bytes = cache_session.get(key)
    return str(response)


def set_value_in_cache(
    cache_session: RedisCluster, key: str, value: str
) -> None:
    expiry = 600  # 10m in seconds
    cache_session.set(name=key, value=value, ex=expiry)
