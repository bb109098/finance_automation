from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level='INFO')
logger.add('logs/system.log', rotation='10 MB')

def get_logger():
    return logger
