import unittest
from sel.POM.youtube import BrowserWrapper
from sel.POM.youtube import ConfigProvider
from sel.POM.youtube import HomePage


class TestDeviceTheme(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_switch_to_hebrew(self):
        self.home_page.click_hebrew_language()
        self.assertEqual(self.home_page.get_first_use_title(),"כדאי להתחיל לחפש")

    def test_switch_to_english(self):
        self.home_page.click_english_language()
        self.assertEqual(self.home_page.get_first_use_title(), "Try searching to get started")


if __name__ == "__main__":
    unittest.main()
