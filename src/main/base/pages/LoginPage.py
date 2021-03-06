#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from src.main.base.BasePage import BasePage
from src.main.base.locators.LoginPageLocators import LoginPageLocators
from src.main.base.pages.RecoverPasswordPage import RecoverPasswordPage
from src.main.utils.Logger import Logger

class LoginPage(BasePage):

    global logger
    logger = Logger(__name__)

    usr_input_field = None
    pwd_input_field = None
    submit_btn = None
    forgot_my_pwd_link = None

    '''
        [Description]
        __init__
        :param driver -> WebDriver Object  
    '''
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.init_elements()

    '''
        [Description]
        init_elements
        :cvar -> Initiation of WebElements
    '''
    def init_elements(self):
        logger.info("{} - init_elements".format(__name__))
        try:
            self.usr_input_field = self._driver.find_element(By.ID, "username")
            logger.debug("{} -> usr_input_field : {}".format(__name__, self.usr_input_field))
            self.pwd_input_field = self._driver.find_element(By.ID, "password")
            logger.debug("{} -> pwd_input_field : {}".format(__name__, self.pwd_input_field))
            self.submit_btn = self._driver.find_element(By.ID, "Login")
            logger.debug("{} -> submit_btn : {}".format(__name__, self.submit_btn))
            self.forgot_my_pwd_link = self._driver.find_element(By.ID, "forgot_password_link")
            logger.debug("{} -> forgot_my_pwd_link : {}".format(__name__, self.forgot_my_pwd_link))
        except Exception as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        login
        :param username -> String Object
        :param password -> String Object
        :return self.msg.text -> String Object
    '''
    def login(self, username, password):
        logger.warn("{} - login : {}, {}".format(__name__, username, password))
        try:
            self.fill_text(self.usr_input_field, username)
            self.fill_text(self.pwd_input_field, password)
            self.click(self.submit_btn)

            self.msg = self.wait_until_visible(LoginPageLocators.ERR_MSG_TEXT)
            return self.msg.text
        except Exception as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e

    '''
        [Description]
        recover_password    
        :return self.msg.text -> String Object
    '''
    def recover_password(self):
        logger.warn("{} - recover_password".format(__name__))
        try:
            self.click(self.forgot_my_pwd_link)
            return RecoverPasswordPage(self._driver)
        except Exception as e:
            logger.error("{} - ERROR : {}".format(__name__, e))
            raise e
