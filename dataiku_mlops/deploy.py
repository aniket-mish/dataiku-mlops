import dataikuapi
from loguru import logger


def deploy() -> str:
    dataikuapi.DSSClient()
    logger.info("deploy function called.")
    return "deploy"
