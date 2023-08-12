import logging
import logging.config
import os

import yaml


def read_logging_config(default_path="logging.yml", env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            logging_config = yaml.safe_load(f.read())
        return logging_config
    else:
        return None


class CustomLogger(logging.getLoggerClass()):
    """custom logger with additional logging levels"""

    SUCCESS = 45
    NOTICE = 35
    VERBOSE = 25
    SPAM = 15

    logging.addLevelName(SUCCESS, "SUCCESS")
    logging.addLevelName(NOTICE, "NOTICE")
    logging.addLevelName(VERBOSE, "VERBOSE")
    logging.addLevelName(SPAM, "SPAM")

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(CustomLogger.SUCCESS):
            self._log(CustomLogger.SUCCESS, msg, args, **kwargs)

    def notice(self, msg, *args, **kwargs):
        if self.isEnabledFor(CustomLogger.NOTICE):
            self._log(CustomLogger.NOTICE, msg, args, **kwargs)

    def verbose(self, msg, *args, **kwargs):
        if self.isEnabledFor(CustomLogger.VERBOSE):
            self._log(CustomLogger.VERBOSE, msg, args, **kwargs)

    def spam(self, msg, *args, **kwargs):
        if self.isEnabledFor(CustomLogger.SPAM):
            self._log(CustomLogger.SPAM, msg, args, **kwargs)
