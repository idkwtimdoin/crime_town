from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")


DB_HOST = config("DB_HOST", default=None)
DB_PORT = config("DB_PORT", cast=int, default=None)
DB_USERNAME = config("DB_USERNAME", default=None)
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default=None)
DB_NAME = config("DB_NAME", default=None)

LOG_QUERIES = config("LOG_QUERIES", cast=bool, default=False)
