from selenium import webdriver
from sel.POM.youtube import ConfigProvider
from selenium.common.exceptions import *


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self._config = ConfigProvider.load_from_file()
        print("Test Start")

    def get_driver(self, page):
        try:
            browser = self._config.get("browser", "Firefox")  # Default to Firefox if not specified
            if browser == "Chrome":
                self._driver = webdriver.Chrome()
            elif browser == "Firefox":
                self._driver = webdriver.Firefox()
            elif browser == "Edge":
                self._driver = webdriver.Edge()
            else:
                raise ValueError(f"Unsupported browser: {browser}")

            url = self._config.get(page)
            if url:
                self._driver.get(url)
                self._driver.implicitly_wait(2)
            else:
                print(f"Page '{page}' not found in the configuration.")
            return self._driver
        except WebDriverException as e:
            print(f"WebDriverException : {e}")
