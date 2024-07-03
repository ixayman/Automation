from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from sel.POM.saucedemo.infra.base_page import BasePage


class BasePageApp(BasePage):
    # MAIN COMPONENTS:
    HEADER_CONTAINER = '//div[@id="header_container"]'
    FOOTER_CONTAINER = '//footer[@class="footer"]'

    # SUB COMPONENTS - HEADER:
    APP_LOGO = '//div[@class = "app_logo"]'
    CART_LINK = '//a[@class="shopping_cart_link"]'
    HAMBURGER_BUTTON = '//button[@id="react-burger-menu-btn"]'

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
        # self._hamburger_button = self._header_container.find_element(By.XPATH, self.HAMBURGER_BUTTON)

        # SUB COMPONENTS - FOOTER:
        self._twitter_logo = self._footer_container.find_element(By.XPATH, self.TWITTER_LINK)
        self._facebook_logo = self._footer_container.find_element(By.XPATH, self.FACEBOOK_LINK)
        self._linkedin_logo = self._footer_container.find_element(By.XPATH, self.LINKEDIN_LINK)
        self._copyright_mark = self._footer_container.find_element(By.XPATH, self.COPYRIGHT_MARK)

    # ----------HEADER--------------
    def get_app_logo(self):
        return self._app_logo.text

    def click_cart_link(self):
        return self._cart_link.click()

    def get_cart_badge_value(self):
        try:
            badge = self._header_container.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            return badge.text
        except NoSuchElementException:
            return 0

    def hamburger_menu_visible(self):
        try:
            menu = self._header_container.find_element(By.XPATH, self.HAMBURGER_BUTTON)
            return True
        except NoSuchElementException:
            return False

    def open_hamburger_menu(self):
        try:
            menu_button = self._header_container.find_element(By.XPATH, self.HAMBURGER_BUTTON)
            menu_button.click()
        except NoSuchElementException:
            print("Hamburger menu button not found")

    def click_hamburger_menu_item(self, item_text):
        try:
            # Find the specific menu item by its text
            menu_item = self._header_container.find_element(By.XPATH, f"//a[text()='{item_text}']")
            menu_item.click()
        except NoSuchElementException:
            print(f"Menu item '{item_text}' not found")

    # -----------FOOTER----------
    def click_twitter_logo(self):
        return self._twitter_logo.click()

    def click_facebook_logo(self):
        return self._facebook_logo.click()

    def click_linkedin_logo(self):
        return self._linkedin_logo.click()

    def get_copyright_mark(self):
        return self._copyright_mark.text
