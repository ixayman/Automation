from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from sel.POM.saucedemo.logic.base_page_app import BasePageApp
from re import sub


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

    def find_inventory_item_by_name(self, item_name):
        for item in self._inventory_items:
            name_element = item.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
            if name_element.text == item_name:
                return item
        raise NoSuchElementException(f"Item with name '{item_name}' not found")

    def click_inventory_item_name(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        name_element = item.find_element(By.XPATH, './/div[@class="inventory_item_name"]')
        name_element.click()

    def get_inventory_item_image(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        return item.find_element(By.TAG_NAME, 'img')

    def click_inventory_item_image(self, item_name):
        image_element = self.get_inventory_item_image(item_name)
        image_element.click()

    def get_inventory_item_button_label(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        button_element = item.find_element(By.TAG_NAME, 'button')
        return button_element.text

    def click_inventory_item_button(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        button_element = item.find_element(By.TAG_NAME, 'button')
        button_element.click()

    def get_inventory_item_description(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        description_element = item.find_element(By.XPATH, './/div[@class="inventory_item_desc"]')
        return description_element.text

    def get_inventory_item_price(self, item_name):
        item = self.find_inventory_item_by_name(item_name)
        price_element = item.find_element(By.XPATH, './/div[@class="inventory_item_price"]')
        numeric_price = sub(r'[^\d.]+', '', price_element.text)
        return numeric_price
