import logging
from omegaconf import OmegaConf, DictConfig

from src.logging_utils import CustomLogger, read_logging_config


# * set logging config before other modules run
logging.config.dictConfig(read_logging_config())
logging.setLoggerClass(CustomLogger)

# * load api config
api_config: DictConfig = OmegaConf.load("src/api_config.yaml")
