from selenium.webdriver.common.by import By
from sel.POM.herokuapp2.infra.base_page import BasePage


class CheckBoxes(BasePage):
    CHECKBOXES = '//input'

    def __init__(self, driver):
        super().__init__(driver)
        self._checkboxes = driver.find_elements(By.XPATH, self.CHECKBOXES)

    @staticmethod
    def check_box(checkbox):
        checkbox.click()

    def get_checked_list(self):
        checked = []
        for checkbox in self._checkboxes:
            if checkbox.is_selected():
                checked.append(checkbox)
        return checked

    def get_unchecked_list(self):
        unchecked = []
        for checkbox in self._checkboxes:
            if not checkbox.is_selected():
                unchecked.append(checkbox)
        return unchecked
