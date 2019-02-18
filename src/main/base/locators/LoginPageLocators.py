#!/usr/bin/env python3
from selenium.webdriver.common.by import By


class LoginPageLocators:

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "Login")

    ERR_MSG_TEXT = (By.ID, "error")


