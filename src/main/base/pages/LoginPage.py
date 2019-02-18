#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from src.main.base.BasePage import BasePage
from src.main.base.locators.LoginPageLocators import LoginPageLocators
from src.main.utils.Logger import Logger

class LoginPage(BasePage):

    global logger
    logger = Logger(__name__)

    usr_input_field = None
    pwd_input_field = None
    submit_btn = None

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
            self.pwd_input_field = self._driver.find_element(By.ID, "password")
            self.submit_btn = self._driver.find_element(By.ID, "Login")
        except () as e:
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

