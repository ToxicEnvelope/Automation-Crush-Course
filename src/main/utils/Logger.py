#!/usr/bin/env python3
from src.main.utils.Config import Config
import logging
import coloredlogs

class Logger:

    def __init__(self, namespace):
        logging.basicConfig(format=Config.get_logger_format(),
                            filename="{0}/{1}-runtime.log".format(Config.get_logs_dir(),
                                                                  Config.get_timestamp()),
                            level=logging.DEBUG
                            )
        self.log = logging.getLogger(namespace)
        coloredlogs.install(level="DEBUG", logger=self.log)


    def info(self, msg):
        self.log.info(msg)

    def warn(self, msg):
        self.log.warning(msg)

    def critical(self, msg):
        self.log.critical(msg)

    def error(self, msg):
        self.log.error(msg)

    def debug(self, msg):
        self.log.debug(msg)


