#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.utils import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from src.main.utils.Wait import Wait
from src.main.utils.Logger import Logger


class BasePage(Wait):


    global logger
    logger = Logger(__name__)

    '''
        [Description]
        __init__
        :param driver -> WebDriver Object
    '''
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        # _js will be used for JavaScript manipulation
        self._js = (
            # synchronous calls
            self._driver.execute_script,
            # asynchronous calls
            self._driver.execute_async_script
        )

    '''
        [Description]
        click_by
        :param webelement -> WebElement Object
    '''
    def click(self, webelement):
        logger.debug("{} - click : {}".format(__name__, webelement))
        try:
            webelement.click() if webelement.is_displayed() else WebDriverException("WebElement is not Clickable...")
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            print(e)
            raise e

    '''
        [Description]
        click_by
        :param by_obj -> By Object
    '''
    def click_by(self, by_obj):
        logger.debug("{} - click : {}".format(__name__, by_obj))
        try:
            prxy = self.wait_until_visible(by_obj)
            prxy.click() if prxy.is_displayed() else WebDriverException("WebElement is not Clickable...")
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        fill_text
        :param webelement -> WebElement Object
        :param phrase -> String Object
    '''
    def fill_text(self, webelement, pharse):
        logger.debug("{} - send_keys : {}, {} ".format(__name__, webelement, pharse))
        try:
            if webelement.is_displayed():
                webelement.send_keys(pharse)
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        get_title
        :return String Object
    '''
    def get_title(self):
        logger.debug("{} - get_title".format(__name__))
        try:
            return self._driver.title
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e
    '''
        [Description]
        get_source_page
        :return DocString Object
    '''
    def get_source_page(self):
        logger.debug("{} - get_source_page".format(__name__))
        try:
            return self._driver.source_page
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        scroll_and_click
        :param webelement -> WebElement Object
    '''
    def scroll_and_click(self, webelement):
        logger.debug("{} - scroll_and_click : {}".format(__name__, webelement))
        try:
            action = ActionChains(self._driver)
            action.move_to_element(webelement) \
                .click_by(webelement) \
                .perform()
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        wait
        :param sec -> Integer Object
    '''
    def wait(self, sec):
        logger.debug("{} - wait : {}".format(__name__, sec))
        try:
            time.sleep(sec)
        except Exception as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        init_elements
        :rtype pass -> Abstract Implementation, will be defined in each POM subclass 
    '''
    def init_elements(self):
        pass

    '''
        [Description]
        switch_default
        :cvar -> Switch back to default iframe
    '''
    def switch_default(self):
        logger.critical("{} - switch_default".format(__name__))
        try:
            self._driver.switch_to.default_content()
        except (Exception, WebDriverWait, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        switch_to
        :param by_obj -> By Object
        :cvar -> Switch to passed iframe By Object
    '''
    def switch_to(self, by_obj):
        logger.critical("{} - switch_to : {}".format(__name__, by_obj))
        try:
            prxy = self.wait_until_invisible(by_obj)
            if prxy.is_displayed():
                self._driver.switch_to.frame(prxy)
        except (Exception, WebDriverWait, StaleElementReferenceException) as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

