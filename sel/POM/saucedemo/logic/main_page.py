from selenium.webdriver.common.by import By
from sel.POM.saucedemo.infra.base_page import BasePage


class MainPage(BasePage):
    # MAIN COMPONENTS:
    HEADER_CONTAINER = '//div[@id="header_container"]'
    INVENTORY_CONTAINER = '//div[@id="inventory_container"]'
    FOOTER = '//footer[@class="footer"]'

    # SUB COMPONENTS - HEADER:
    APP_LOGO = '//div[@class = "app_logo"]'
    CART_LINK = '//a[@class="shopping_cart_link"]'
    HAMBURGER_MENU = '//button[@id="react-burger-menu-btn"]'

    # SUB COMPONENTS - INVENTORY:

    def __init__(self, driver):
        super().__init__(driver)
        # MAIN COMPONENTS:
        self._header_container = self._driver.find_element(By.XPATH, self.HEADER_CONTAINER)
        self._inventory_container = self._driver.find_element(By.XPATH, self.INVENTORY_CONTAINER)
        self._footer = self._driver.find_element(By.XPATH, self.FOOTER)

        # SUB COMPONENTS - HEADER:
        self._app_logo = self._header_container.find_element(By.XPATH, self.APP_LOGO)
        self._cart_link = self._header_container.find_element(By.XPATH, self.CART_LINK)
        self._hamburger_menu = self._header_container.find_element(By.XPATH, self.HAMBURGER_MENU)

        # SUB COMPONENTS - INVENTORY:
