from selenium.webdriver.common.by import By

from sel.POM.herokuapp.infra.base_page import BasePage


class HomePage(BasePage):
    MAIN_HEADER_TITLE = (By.XPATH, '//h1')
    SUB_HEADER_TITLE = (By.XPATH, '//h3')
    MAKE_APPOINTMENT_BUTTON = (By.XPATH, '//a[@id="menu-toggle"]')
    HAMBURGER_BUTTON = (By.XPATH, '//i[@class="fa fa-bars"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._main_header_title = self._driver.find_element(self.MAIN_HEADER_TITLE)
        self._sub_header_title = self._driver.find_element(self.SUB_HEADER_TITLE)
        self._make_appointment_button = self._driver.find_element(self.MAKE_APPOINTMENT_BUTTON)
        self._hamburger_button = self._driver.find_element(self.HAMBURGER_BUTTON)

    def get_main_title_header_string(self):
        return self._main_header_title.text

    def get_sub_header_title_string(self):
        return self._sub_header_title.text

    def click_make_appointment_button(self):
        self._make_appointment_button.click()

    def click_hamburger_button(self):
        self._hamburger_button.click()
