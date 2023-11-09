import os
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

# SQLAlchemy
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.pool import StaticPool

#
from app.config import config
#
from app.logger import logger
#
from app.utils.metaclasses import SingletonMeta


#
class Base(DeclarativeBase):
    pass


class Database(metaclass=SingletonMeta):
    def __init__(self, db_url: str):
        connect_args = {}
        if "sqlite" in db_url:
            logger.info("sqlite database detected!")
            connect_args = {"check_same_thread": False}
        self._engine = create_engine(db_url, echo=True, connect_args=connect_args)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_all(self) -> None:
        """Creates database tables."""
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()


# dbdir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
# db_url = "sqlite:///" + os.path.join(dbdir, "db.sqlite3")
db_url = config.DB_URL
db_url = db_url.replace("mysql", "mysql+pymysql")


db = Database(db_url=db_url)
db.create_all()
