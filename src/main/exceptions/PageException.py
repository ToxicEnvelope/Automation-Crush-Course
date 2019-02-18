#!/usr/bin/env python3
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException


class PageException(Exception):

    def __init__(self, msg, *args, **kwargs):
            WebDriverException(msg, args, kwargs) or StaleElementReferenceException(msg, args, kwargs)

