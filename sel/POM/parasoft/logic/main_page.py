from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from sel.POM.parasoft.logic.base_page_app import BasePageApp
from re import sub


class MainPage(BasePageApp):
    REGISTER_LINK = '//a[contains(text() = "register")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._register_link = self._driver.find_element(By.XPATH, self.REGISTER_LINK)

    def click_register_link(self):
        return self._register_link.click()