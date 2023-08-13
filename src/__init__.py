import logging

from src.logging_utils import CustomLogger, read_logging_config


# * set logging config before other modules run
logging.config.dictConfig(read_logging_config())
logging.setLoggerClass(CustomLogger)
