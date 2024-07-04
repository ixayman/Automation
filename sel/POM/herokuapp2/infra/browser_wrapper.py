from selenium import webdriver
from sel.POM.herokuapp2.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self._config = ConfigProvider.load_from_file('../config.json')
        print("Test Start")

    def get_driver(self, url):
        browser = self._config.get("browser", "Firefox")  # Default to Firefox if not specified
        if browser == "Chrome":
            self._driver = webdriver.Chrome()
        elif browser == "Firefox":
            self._driver = webdriver.Firefox()
        elif browser == "Edge":
            self._driver = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
