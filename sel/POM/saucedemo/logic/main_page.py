from selenium.webdriver.common.by import By
from sel.POM.saucedemo.infra.base_page_app import BasePageApp


class MainPage(BasePageApp):
    # MAIN COMPONENTS:
    INVENTORY_CONTAINER = '//div[@id="inventory_container"]'
    # SUB COMPONENTS - INVENTORY:
    INVENTORY_ITEMS = '//div[@class="inventory_item"]'

    def __init__(self, driver):
        super().__init__(driver)
        # MAIN COMPONENTS:
        self._inventory_container = self._driver.find_element(By.XPATH, self.INVENTORY_CONTAINER)

        # SUB COMPONENTS - INVENTORY:
        self._inventory_items = self._inventory_container.find_elements(By.XPATH, self.INVENTORY_ITEMS)

    def get_inventory_item_name(self, number):
        item = self._inventory_items[number]
        return item.find_element(By.XPATH, '//div[@class="inventory_item_name "]')

    def get_inventory_item_image(self, number):
        item = self._inventory_items[number]
        return item.find_element(By.TAG_NAME, 'img')

    def get_inventory_item_description(self, number):
        item = self._inventory_items[number]
        return item.find_element(By.TAG_NAME, '//div[@class="inventory_item_desc"]')

    def click_inventory_item_name(self, number):
        self.get_inventory_item_name(number).click()

    def click_inventory_item_image(self, number):
        self.get_inventory_item_image(number).click()

    def click_inventory_item_add_button(self, number):
        item = self._inventory_items[number]
        item.find_element(By.TAG_NAME, 'button').click()
