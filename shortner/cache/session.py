from typing import Generator

from rediscluster import RedisCluster

from shortner.settings import Settings


def get_session() -> Generator[RedisCluster, None, None]:
    settings = Settings()

    startup_nodes = [
        {
            'host': f'{settings.REDIS_CACHE_HOST}.default.svc.cluster.local',
            'port': 6379,
        }
    ]
    with RedisCluster(
        startup_nodes=startup_nodes, decode_responses=True
    ) as redis:
        yield redis
