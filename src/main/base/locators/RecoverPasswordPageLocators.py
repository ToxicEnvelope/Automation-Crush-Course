#!/usr/bin/env python3
from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:

    SANDBOX_LOGIN_LNK = (By.ID, "sandbox-login")
    USERNAME_FIELD = (By.ID, "un")
    CANCEL_BTN = (By.CSS_SELECTOR, "div > a")
    CONTINUE_BTN = (By.ID, "continue")
    NEED_HELP_LNK = (By.ID, "video-link")

    ERR_MSG_TEXT = (By.CLASS_NAME, "error")


