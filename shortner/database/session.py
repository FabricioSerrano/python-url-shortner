from typing import Generator

from cassandra.cluster import Cluster, Session

from shortner.settings import Settings


def get_session() -> Generator[Session, None, None]:
    """Handles and returns database session"""
    settings = Settings()

    cluster = Cluster([settings.DATABASE_IP])

    with cluster.connect('shortner') as session:
        yield session

    cluster.shutdown()
