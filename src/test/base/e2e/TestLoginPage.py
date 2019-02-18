#!/usr/bin/env python3
from src.main.utils.Logger import Logger
from src.test.base.BaseTest import BaseTest
from src.main.base.pages.LoginPage import LoginPage
from src.main.exceptions.PageException import PageException
import unittest


class TestLoginPage(BaseTest, unittest.TestCase):

    global logger
    logger = Logger(__name__)

    URL = "https://login.salesforce.com/?"

    INVALID_USERNAME = "yahav@automation.co.il"
    INVALID_PASSWORD = "password1"

    VALID_USERNAME = "gal"
    VALID_PASSWORD = "Aa123456"

    EXPECTED_ERR_MSG = \
        "Please check your username and password. If you still can't log in, contact your Salesforce administrator."


    '''
        [Description]
        test_valid_attempt_to_authenticate
        :cvar -> This test scenario will simulate a valid login authentication
    '''
    def test_valid_attempt_to_authenticate(self):
        try:
            st = self.timer()

            logger.debug("{} - test_valid_attempt_to_authenticate".format(__name__))
            driver = self.driver

            logger.info("{} - GET -> {}".format(__name__, self.URL))
            driver.get(self.URL)

            lp = LoginPage(driver)
            msg_txt = lp.login(self.VALID_USERNAME, self.VALID_PASSWORD)
            logger.debug("{} - AssertEquals -> expected: {} | actual: {}".format(__name__, self.EXPECTED_ERR_MSG,
                                                                                 msg_txt))
            self.assertEqual(self.EXPECTED_ERR_MSG, msg_txt)

            et = self.timer()
            logger.debug("{} - test_valid_attempt_to_authenticate took {} seconds".format(__name__, et - st))
        except PageException as e:
            logger.warn("{} - WARNING : {}".format(__name__, e))
            logger.error("{} - ERROR : {}".format(__name__, e))

    '''
        [Description]
        test_invalid_attempt_to_authenticate
        :cvar -> This test scenario will simulate a valid login authentication
    '''
    def test_invalid_attempt_to_authenticate(self):
        try:
            st = self.timer()

            logger.debug("{} - test_invalid_attempt_to_authenticate".format(__name__))
            driver = self.driver

            logger.info("{} - GET -> {}".format(__name__, self.URL))
            driver.get(self.URL)

            lp = LoginPage(driver)
            msg_txt = lp.login(self.INVALID_USERNAME, self.INVALID_PASSWORD)
            logger.debug("{} - AssertEquals -> expected: {} | actual: {}".format(__name__, self.EXPECTED_ERR_MSG,
                                                                                 msg_txt))
            self.assertEqual(self.EXPECTED_ERR_MSG, msg_txt)

            et = self.timer()
            logger.debug("{} - test_valid_attempt_to_authenticate took {} seconds".format(__name__, et - st))
        except PageException as e:
            logger.warn("{} - WARNING : {}".format(__name__, e))
            logger.error("{} - ERROR : {}".format(__name__, e))


if __name__ == '__main__':
    unittest.main()
