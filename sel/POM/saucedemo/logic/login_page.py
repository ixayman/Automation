from sel.POM.saucedemo.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_LOGO = '//div[@class = "login_logo"]'
    USER_NAME_FIELD = '//input[@id = "user-name"]'
    PASSWORD_FIELD = '//input[@id = "password"]'
    LOGIN_BUTTON = '//input[@id = "login-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._login_logo = self._driver.find_element(By.XPATH, self.LOGIN_LOGO)
        self._user_name_field = self._driver.find_element(By.XPATH, self.USER_NAME_FIELD)
        self._password_field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def get_login_logo(self):
        return self._login_logo.text

    def insert_in_user_name_field(self, username):
        self._user_name_field.clear()
        self._user_name_field.send_keys(username)

    def insert_in_password_field(self, password):
        self._password_field.clear()
        self._password_field.send_keys(password)

    def click_login_button(self):
        self._login_button.click()
