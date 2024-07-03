from sel.POM.saucedemo.logic.login_page import LoginPage
from sel.POM.saucedemo.infra.browser_wrapper import BrowserWrapper
import unittest
from selenium import webdriver


class TestLoginPage:
    browser_wrapper = BrowserWrapper()
    driver = browser_wrapper.get_driver('https://www.saucedemo.com/')
    login_page = LoginPage(driver)

    def test_login_logo(self):
        phrase = "Swag Labs"
        if phrase == self.login_page.get_login_logo():
            print("TEST PASSED")
        else:
            print("TEST FAILED")


temp = TestLoginPage()
temp.test_login_logo()
