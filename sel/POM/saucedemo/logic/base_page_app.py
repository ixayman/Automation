from selenium.webdriver.common.by import By

from sel.POM.saucedemo.infra.base_page import BasePage


class BasePageApp(BasePage):
    # MAIN COMPONENTS:
    HEADER_CONTAINER = '//div[@id="header_container"]'
    FOOTER_CONTAINER = '//footer[@class="footer"]'

    # SUB COMPONENTS - HEADER:
    APP_LOGO = '//div[@class = "app_logo"]'
    CART_LINK = '//a[@class="shopping_cart_link"]'
    HAMBURGER_MENU = '//button[@id="react-burger-menu-btn"]'

    # SUB COMPONENTS - FOOTER:
    TWITTER_LINK = '//a[contains(@href, "twitter")]'
    FACEBOOK_LINK = '//a[contains(@href, "facebook")]'
    LINKEDIN_LINK = '//a[contains(@href, "linkedin")]'
    COPYRIGHT_MARK = '//div[@class = "footer_copy")]'

    def __init__(self, driver):
        super().__init__(driver)
        # MAIN COMPONENTS:
        self._header_container = self._driver.find_element(By.XPATH, self.HEADER_CONTAINER)
        self._footer_container = self._driver.find_element(By.XPATH, self.FOOTER_CONTAINER)

        # SUB COMPONENTS - HEADER:
        self._app_logo = self._header_container.find_element(By.XPATH, self.APP_LOGO)
        self._cart_link = self._header_container.find_element(By.XPATH, self.CART_LINK)
        self._hamburger_menu = self._header_container.find_element(By.XPATH, self.HAMBURGER_MENU)

        # SUB COMPONENTS - FOOTER:
        self._twitter_logo = self._footer_container.find_element(By.XPATH, self.TWITTER_LINK)
        self._facebook_logo = self._footer_container.find_element(By.XPATH, self.FACEBOOK_LINK)
        self._linkedin_logo = self._footer_container.find_element(By.XPATH, self.LINKEDIN_LINK)
        self._copyright_mark = self._footer_container.find_element(By.XPATH, self.COPYRIGHT_MARK)

    def get_app_logo(self):
        return self._app_logo.text

    def click_cart_link(self):
        return self._cart_link.click()

    def click_hamburger_menu(self):
        return self._hamburger_menu.click()

    def click_twitter_logo(self):
        return self._twitter_logo.click()

    def click_facebook_logo(self):
        return self._facebook_logo.click()

    def click_linkedin_logo(self):
        return self._linkedin_logo.click()

    def get_copyright_mark(self):
        return self._copyright_mark.text
