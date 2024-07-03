import json
from selenium import webdriver
from sel.POM.saucedemo.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self._config = ConfigProvider.load_from_file('config.json')
        print("Test Start")

    def get_driver(self, url):
        if self._config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self._config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self._config["browser"] == "Edge":
            self._driver = webdriver.Edge()
        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
