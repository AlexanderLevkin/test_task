from loguru import logger
import sys

logger.add(sys.stderr,
           format="| <cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> | <blue>{message}</blue> ",
           colorize=True)
logger.remove(0)
