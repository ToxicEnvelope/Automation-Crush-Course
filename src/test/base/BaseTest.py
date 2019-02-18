#!/usr/bin/env python3
import time
from selenium import webdriver
from src.main.utils.Config import Config
from src.main.utils.Logger import Logger
import unittest

class BaseTest:


    global logger
    logger = Logger(__name__)

    driver = None

    '''
        [Description]
        setUp
        :cvar -> Responsible to initialize the WebDriver Object and configurations    
    '''
    def setUp(self):
        logger.info("{} - setUp".format(__name__))
        self.driver = webdriver.Chrome(Config.get_driver('chrome'))
        self.driver.maximize_window()

    '''
        [Description]
        tearDown
        :cvar -> Responsible to close and quit all WebDriver sessions      
    '''
    def tearDown(self):
        logger.info("{} - tearDown".format(__name__))
        if self.driver:
            logger.info("{} - closing...".format(__name__))
            self.driver.close()
            logger.info("{} - quiting...".format(__name__))
            self.driver.quit()

    @staticmethod
    def timer():
        return int(time.time().__str__()[:10])



if __name__ == '__main__':
    unittest.main()
