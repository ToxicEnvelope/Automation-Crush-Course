#!/usr/bin/env python3
from os.path import expanduser
import platform
import time

class Config:

    @staticmethod
    def get_logs_dir():
        return expanduser("~/Desktop/Git/Automation-Crush-Course/logs")

    @staticmethod
    def get_test_resources_dir():
        return expanduser("~/Desktop/Git/Automation-Crush-Course/src/test/resources")

    @staticmethod
    def get_bin_dir():
        return expanduser("~/Desktop/Git/Automation-Crush-Course/bin")

    @classmethod
    def get_driver(cls, driver_name):
        p = platform.platform()
        p = p.lower()
        if p.startswith('win'):
            if driver_name.lower().__eq__('chrome'):
                return cls.get_bin_dir() + "/chromedriver.exe"
            elif driver_name.lower().__eq__('geck'):
                return cls.get_bin_dir() + "/geckodriver.exe"
        else:
            if driver_name.lower().__eq__('chrome'):
                return cls.get_bin_dir() + "/chromedriver"
            elif driver_name.lower().__eq__('geck'):
                return cls.get_bin_dir() + "/geckodriver"

    @staticmethod
    def get_logger_format():
        return "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @staticmethod
    def get_timestamp():
        return time.time().__str__()[:10]

