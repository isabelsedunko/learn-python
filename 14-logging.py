import logging
# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename="c:\\python\\restaurant.log", level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()
logger.info("The Restaurant Is Open")
print(logger.level)

