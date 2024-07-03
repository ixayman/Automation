from sel.POM.saucedemo.logic.login_page import LoginPage
import unittest
from selenium import webdriver


class TestLoginPage:
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    def test_loin_logo(self):
        phrase = "Swag Labs"
        if phrase == self.login_page.get_login_logo():
            print("TEST PASSED")
        else:
            print("TEST FAILED")


temp = TestLoginPage()
temp.test_loin_logo()

