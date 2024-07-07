from sel.POM.parasoft.logic.register_page import RegisterPage
from sel.POM.parasoft.infra.browser_wrapper import BrowserWrapper
import unittest
from selenium import webdriver
from sel.POM.parasoft.infra.config_provider import ConfigProvider
from sel.POM.parasoft.infra.utils import generate_random_string


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("register_page")
        self.register_page = RegisterPage(self.driver)
        self.config = ConfigProvider()

    def tearDown(self):
        self.driver.close()

    def input_register_data(self, reg_list):
        self.register_page.insert_in_first_name_field(reg_list[0])
        self.register_page.insert_in_last_name_field(reg_list[1])
        self.register_page.insert_in_address_field(reg_list[2])
        self.register_page.insert_in_city_field(reg_list[3])
        self.register_page.insert_in_state_field(reg_list[4])
        self.register_page.insert_in_zip_code_field(reg_list[5])
        self.register_page.insert_in_phone_number_field(reg_list[6])
        self.register_page.insert_in_ssn_field(reg_list[7])
        self.register_page.insert_in_username_field(reg_list[8])
        self.register_page.insert_in_password_field(reg_list[9])
        self.register_page.insert_in_confirm_password_field(reg_list[10])

    def test_register_success(self):
        reg_list = [self.config.get_value(self, "FIRST_NAME"),
                    self.config.get_value(self, "LAST_NAME"),
                    self.config.get_value(self, "ADDRESS"),
                    self.config.get_value(self, "CITY"),
                    self.config.get_value(self, "STATE"),
                    self.config.get_value(self, "ZIP_CODE"),
                    self.config.get_value(self, "PHONE_NUMBER"),
                    self.config.get_value(self, "SSN"),
                    generate_random_string(8),
                    self.config.get_value(self, "PASSWORD"),
                    self.config.get_value(self, "PASSWORD")]
        self.input_register_data(reg_list)
        self.register_page.click_register_button()
        self.assertIn(self.config.get_value(self, "ACCOUNT_CREATED"), self.register_page.get_account_created_msg())

    def test_register_non_matching_passwords(self):
        reg_list = [self.config.get_value(self, "FIRST_NAME"),
                    self.config.get_value(self, "LAST_NAME"),
                    self.config.get_value(self, "ADDRESS"),
                    self.config.get_value(self, "CITY"),
                    self.config.get_value(self, "STATE"),
                    self.config.get_value(self, "ZIP_CODE"),
                    self.config.get_value(self, "PHONE_NUMBER"),
                    self.config.get_value(self, "SSN"),
                    generate_random_string(8),
                    self.config.get_value(self, "PASSWORD"),
                    generate_random_string(8)]
        self.input_register_data(reg_list)
        self.register_page.click_register_button()
        self.assertIn(self.config.get_value(self, "NON_MATCHING_PASSWORDS_ERROR"),
                      self.register_page.get_non_matching_passwords_error())

    def test_unavailable_username(self):
        reg_list = [self.config.get_value(self, "FIRST_NAME"),
                    self.config.get_value(self, "LAST_NAME"),
                    self.config.get_value(self, "ADDRESS"),
                    self.config.get_value(self, "CITY"),
                    self.config.get_value(self, "STATE"),
                    self.config.get_value(self, "ZIP_CODE"),
                    self.config.get_value(self, "PHONE_NUMBER"),
                    self.config.get_value(self, "SSN"),
                    self.config.get_value(self, "USERNAME"),
                    self.config.get_value(self, "PASSWORD"),
                    self.config.get_value(self, "PASSWORD")]
        self.input_register_data(reg_list)
        self.register_page.click_register_button()
        self.assertIn(self.config.get_value(self, "UNAVAILABLE_USERNAME"),
                      self.register_page.get_unavailable_username())
