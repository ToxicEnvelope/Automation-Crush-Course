#!/usr/bin/env python3
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.utils.Logger import Logger

class Wait:

    global logger
    logger = Logger(__name__)

    '''
        [Description]
        __init__
        :param driver -> WebDriver Object
    '''
    def __init__(self, driver):
        self._driver = driver


    '''
        [Description]
        wait_until_visible
        :param driver -> By Object
    '''
    def wait_until_visible(self, by_obj):
        logger.critical("{} - wait_until_visible : {}".format(__name__, by_obj))
        try:
            return WebDriverWait(self._driver, 15, 300).until(EC.visibility_of_element_located(by_obj))
        except () as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        wait_until_clickable
        :param driver -> By Object
    '''
    def wait_until_clickable(self, by_obj):
        logger.critical("{} - wait_until_clickable : {}".format(__name__, by_obj))
        try:
            return WebDriverWait(self._driver, 15, 300).until(EC.element_to_be_clickable(by_obj))
        except () as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        wait_until_invisible
        :param driver -> By Object
    '''
    def wait_until_invisible(self, by_obj):
        logger.critical("{} - wait_until_invisible : {}".format(__name__, by_obj))
        try:
            return WebDriverWait(self._driver, 15, 300).until(EC.invisibility_of_element_located(by_obj))
        except () as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e




