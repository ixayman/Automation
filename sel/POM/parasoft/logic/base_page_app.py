from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from sel.POM.parasoft.infra.base_page import BasePage


class BasePageApp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


