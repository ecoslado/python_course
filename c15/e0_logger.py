__author__ = 'enriquecoslados'

import logging

FORMAT = "%(levelname)s: %(asctime)s %(filename)s %(funcName)s %(message)s"
import datetime
# FORMATTER
formatter = logging.Formatter(FORMAT)

# HANDLER
handler = logging.FileHandler("myproject-%s.log" % datetime.datetime.now().strftime("%Y-%m-%d"))
handler.setFormatter(formatter)


# LOGGER
logger = logging.getLogger("MyProject")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

