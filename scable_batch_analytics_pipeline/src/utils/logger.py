import logging
import logging.config
import yaml


def get_logger():

    with open("configs/logging.yaml") as file:
        config = yaml.safe_load(file)

    logging.config.dictConfig(config)

    return logging.getLogger(__name__)