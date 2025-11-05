from rediscluster import RedisCluster


def increment_counter(counter_session: RedisCluster) -> int | None:
    try:
        value = counter_session.incr('url_counter')

        return value

    except Exception:
        return None
