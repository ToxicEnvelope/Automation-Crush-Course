#!/usr/bin/env python3
from src.main.utils.Logger import Logger
from src.test.base.BaseTest import BaseTest
from src.main.base.pages.LoginPage import LoginPage
import unittest


class TestLoginPage(BaseTest, unittest.TestCase):

    global logger
    logger = Logger(__name__)

    URL = "https://login.salesforce.com/?"

    INVALID_USERNAME = "yahav@automation.co.il"
    INVALID_PASSWORD = "password1"

    ERROR_TXT_MSG = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."

    VALID_USERNAME = "gal"
    VALID_PASSWORD = "Aa123456"


    '''
        [Description]
        test_valid_attempt_to_authenticate
        :cvar -> This test scenario will simulate a valid login authentication
    '''
    def test_valid_attempt_to_authenticate(self):
        st = self.timer()

        logger.debug("{} - test_valid_attempt_to_authenticate".format(__name__))
        driver = self.driver

        logger.info("{} - GET -> {}".format(__name__, self.URL))
        driver.get(self.URL)

        lp = LoginPage(driver)
        msg_txt = lp.login(self.VALID_USERNAME, self.VALID_PASSWORD)
        logger.debug("{} - AssertEquals -> expected: {} | actual: {}".format(__name__, self.ERROR_TXT_MSG, msg_txt))
        self.assertEqual(self.ERROR_TXT_MSG, msg_txt)

        et = self.timer()
        logger.debug("{} - test_valid_attempt_to_authenticate took {} seconds".format(__name__, et - st))

    '''
        [Description]
        test_invalid_attempt_to_authenticate
        :cvar -> This test scenario will simulate a valid login authentication
    '''
    def test_invalid_attempt_to_authenticate(self):
        st = self.timer()

        logger.debug("{} - test_invalid_attempt_to_authenticate".format(__name__))
        driver = self.driver

        logger.info("{} - GET -> {}".format(__name__, self.URL))
        driver.get(self.URL)

        lp = LoginPage(driver)
        msg_txt = lp.login(self.INVALID_USERNAME, self.INVALID_PASSWORD)
        logger.debug("{} - AssertEquals -> expected: {} | actual: {}".format(__name__, self.ERROR_TXT_MSG, msg_txt))
        self.assertEqual(self.ERROR_TXT_MSG, msg_txt)

        et = self.timer()
        logger.debug("{} - test_valid_attempt_to_authenticate took {} seconds".format(__name__, et - st))


if __name__ == '__main__':
    unittest.main()