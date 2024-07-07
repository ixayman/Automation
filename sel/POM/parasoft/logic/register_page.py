from sel.POM.parasoft.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class RegisterPage(BasePage):
    FIRST_NAME = '//input[contains(@name, "firstName")]'
    LAST_NAME = '//input[contains(@name, "lastName")]'
    ADDRESS = '//input[contains(@name, "address.street")]'
    CITY = '//input[contains(@name, "address.city")]'
    STATE = '//input[contains(@name, "address.state")]'
    ZIP_CODE = '//input[contains(@name, "address.zipCode")]'
    PHONE_NUMBER = '//input[contains(@name, "phoneNumber")]'
    SSN = '//input[contains(@name, "ssn")]'
    USERNAME = '//input[contains(@name, "customer.username")]'
    PASSWORD = '//input[contains(@name, "customer.password")]'
    CONFIRM_PASSWORD = '//input[contains(@name, "repeatedPassword")]'
    REGISTER_BUTTON = '//input[contains(@value, "Register")]'
    ACCOUNT_CREATED = '//p[contains(text(),  "Your account was created successfully")]'
    NON_MATCHING_PASSWORDS_ERROR = '//span[contains(@id, "repeatedPassword.errors")]'
    UNAVAILABLE_USERNAME = '//span[contains(@id, "customer.username.errors")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._first_name = self._driver.find_element(By.XPATH, self.FIRST_NAME)
        self._last_name = self._driver.find_element(By.XPATH, self.LAST_NAME)
        self._address = self._driver.find_element(By.XPATH, self.ADDRESS)
        self._city = self._driver.find_element(By.XPATH, self.CITY)
        self._state = self._driver.find_element(By.XPATH, self.STATE)
        self._zip_code = self._driver.find_element(By.XPATH, self.ZIP_CODE)
        self._phone_number = self._driver.find_element(By.XPATH, self.PHONE_NUMBER)
        self._ssn = self._driver.find_element(By.XPATH, self.SSN)
        self._username = self._driver.find_element(By.XPATH, self.USERNAME)
        self._password = self._driver.find_element(By.XPATH, self.PASSWORD)
        self._confirm_password = self._driver.find_element(By.XPATH, self.CONFIRM_PASSWORD)
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def insert_in_first_name_field(self, value):
        self._first_name.clear()
        self._first_name.send_keys(value)

    def insert_in_last_name_field(self, value):
        self._last_name.clear()
        self._last_name.send_keys(value)

    def insert_in_address_field(self, value):
        self._address.clear()
        self._address.send_keys(value)

    def insert_in_city_field(self, value):
        self._city.clear()
        self._city.send_keys(value)

    def insert_in_state_field(self, value):
        self._state.clear()
        self._state.send_keys(value)

    def insert_in_zip_code_field(self, value):
        self._zip_code.clear()
        self._zip_code.send_keys(value)

    def insert_in_phone_number_field(self, value):
        self._phone_number.clear()
        self._phone_number.send_keys(value)

    def insert_in_ssn_field(self, value):
        self._ssn.clear()
        self._ssn.send_keys(value)

    def insert_in_username_field(self, value):
        self._username.clear()
        self._username.send_keys(value)

    def insert_in_password_field(self, value):
        self._password.clear()
        self._password.send_keys(value)

    def insert_in_confirm_password_field(self, value):
        self._confirm_password.clear()
        self._confirm_password.send_keys(value)

    def click_register_button(self):
        self._register_button.click()

    def get_account_created_msg(self):
        return self._driver.find_element(By.XPATH, self.ACCOUNT_CREATED).text

    def get_non_matching_passwords_error(self):
        return self._driver.find_element(By.XPATH, self.NON_MATCHING_PASSWORDS_ERROR).text

    def get_unavailable_username(self):
        return self._driver.find_element(By.XPATH, self.UNAVAILABLE_USERNAME).text
