import logging.config

from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src import config


logger = logging.getLogger(__name__)


def obfuscate_creds(url: str) -> str:
    return str(make_url(url).set(username="***", password="***"))


def _get_mysql_config():
    db_conf = dict()

    db_conf["sqlalchemy_database_url"] = (
        f"mysql+pymysql://{config.DB_USERNAME}:{config.DB_PASSWORD}"
        f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )

    db_conf["connect_args"] = {
        "check_same_thread": False,
        "use_prepared_statements": False,
        "connection_load_balance": None,
        "backup_server_node": None,
    }

    db_conf["pool_conf"] = NullPool
    db_conf["echo"] = config.LOG_QUERIES

    return db_conf


def _get_orm_engine():
    db_conf = _get_mysql_config()

    url_to_log = obfuscate_creds(db_conf["sqlalchemy_database_url"])
    logger.debug(f"conn to db: {url_to_log}")

    return create_engine(
        db_conf["sqlalchemy_database_url"],
        connect_args=db_conf["connect_args"],
        echo=db_conf["echo"],
        **db_conf["pool_conf"],
    )


def _get_sessionmaker(engine, expire_on_commit=True) -> sessionmaker:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=expire_on_commit)


Base = declarative_base()
engine = _get_orm_engine()


async def get_db():
    db = _get_sessionmaker(_get_orm_engine())()
    try:
        yield db
    finally:
        db.close()
