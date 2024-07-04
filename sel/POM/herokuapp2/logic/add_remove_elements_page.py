from selenium.webdriver.common.by import By
from sel.POM.herokuapp2.infra.base_page import BasePage


class AddRemoveElements(BasePage):
    ADD_ELEMENT = '//button[text()="Add Element"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_element = driver.find_element(By.XPATH, self.ADD_ELEMENT)

    def click_add_element(self):
        self._add_element.click()

    def add_multiple_elements(self, count):
        for _ in range(count):
            self.click_add_element()

    def get_delete_buttons_list(self):
        return self._driver.find_elements(By.XPATH, '//button[text()="Delete"]')

    def click_delete_button(self):
        while self.get_delete_buttons_list():
            delete_buttons = self.get_delete_buttons_list()
            delete_buttons[0].click()
