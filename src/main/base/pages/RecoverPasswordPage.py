#!/usr/bin/env python3
from src.main.utils.Logger import Logger
from src.main.base.BasePage import BasePage
from selenium.webdriver.common.by import By
from src.main.base.locators.RecoverPasswordPageLocators import RecoverPasswordPageLocators


class RecoverPasswordPage(BasePage, RecoverPasswordPageLocators):

        global logger
        logger = Logger(__name__)

        sandbox_login_link = None
        username_field = None
        cancel_btn = None
        continue_btn = None
        need_help_link = None

        '''
            [Description]
            __init__
            :param driver -> WebDriver Object  
        '''

        def __init__(self, driver):
            super(RecoverPasswordPage, self).__init__(driver)
            self.init_elements()

        '''
            [Description]
            init_elements
            :cvar -> Initiation of WebElements
        '''
        def init_elements(self):
            logger.info("{} - init_elements".format(__name__))
            try:
                self.sandbox_login_link = self._driver.find_element(By.ID, "sandbox-login")
                logger.debug("{} -> sandbox_login_link : {}".format(__name__, self.sandbox_login_link))
                self.username_field = self._driver.find_element(By.ID, "un")
                logger.debug("{} -> username_field : {}".format(__name__, self.username_field))
                self.cancel_btn = self._driver.find_element(By.CSS_SELECTOR, "div > a")
                logger.debug("{} -> cancel_btn : {}".format(__name__, self.cancel_btn))
                self.continue_btn = self._driver.find_element(By.ID, "continue")
                logger.debug("{} -> continue_btn : {}".format(__name__, self.continue_btn))
                self.need_help_link = self._driver.find_element(By.ID, "video-link")
                logger.debug("{} -> need_help_link : {}".format(__name__, self.need_help_link))
            except Exception as e:
                logger.error("{} - ERROR : {}".format(__name__, e))
                raise e

        '''
            [Description]
            recover
            :param uaername -> String Object
            :cvar -> Initiation of WebElements
        '''
        def recover(self, username):
            logger.info("{} - recover : {}".format(__name__, username))
            try:
                self.fill_text(self.username_field, username)
                self.click(self.continue_btn)
                prxy = self.wait_until_visible(RecoverPasswordPageLocators.ERR_MSG_TEXT)
                return prxy.text
            except Exception as e:
                logger.error("{} - ERROR : {}".format(__name__, e))
                raise e

        '''
            [Description]
            info
            :cvar -> will print teh metadata of class RecoverPasswordPage Objects   
        '''
        def into(self):
            print({
                "SANDBOX_LINK": self.sandbox_login_link,
                "USERNAME_FIELD": self.username_field,
                "CANCEL_BTN": self.cancel_btn,
                "CONTINUE_BTN": self.continue_btn,
                "NEED_HELP_LINK": self.need_help_link
            })


