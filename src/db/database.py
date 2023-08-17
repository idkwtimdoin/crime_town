import logging.config

from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from sqlalchemy.orm.decl_api import DeclarativeMeta

from src import config


logger = logging.getLogger(__name__)


def obfuscate_creds(url: str) -> str:
    return str(make_url(url).set(username="*****", password="*****"))


def _get_mysql_config() -> dict:
    db_conf = dict()

    db_conf["sqlalchemy_database_url"] = (
        f"mysql+pymysql://{config.DB_USERNAME}:{config.DB_PASSWORD}"
        f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )

    db_conf["pool_conf"] = dict(poolclass=NullPool)
    db_conf["echo"] = config.LOG_QUERIES

    return db_conf


def _get_orm_engine():
    db_conf = _get_mysql_config()

    url_to_log = obfuscate_creds(db_conf["sqlalchemy_database_url"])
    logger.debug(f"conn to db: {url_to_log}")

    return create_engine(
        db_conf["sqlalchemy_database_url"],
        echo=db_conf["echo"],
        **db_conf["pool_conf"],
    )


def _get_sessionmaker(engine, expire_on_commit=True) -> sessionmaker:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=expire_on_commit)


Base: DeclarativeMeta = declarative_base()
engine = _get_orm_engine()


async def get_db() -> Session:
    db: Session = _get_sessionmaker(_get_orm_engine())()
    try:
        yield db
    finally:
        db.close()
