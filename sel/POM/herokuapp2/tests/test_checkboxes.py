from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from sel.POM.herokuapp2.infra.browser_wrapper import BrowserWrapper
from sel.POM.herokuapp2.logic.checkboxes_page import CheckBoxes


def get_driver():
    browser_wrapper = BrowserWrapper()
    driver = browser_wrapper.get_driver('https://the-internet.herokuapp.com/checkboxes')
    return driver


class TestCheckboxes:
    driver = get_driver()
    add_remove_elements = CheckBoxes(driver)

    def test_enable_all_checkboxes(self):

        unchecked = self.add_remove_elements.get_unchecked_list()
        for item in unchecked:
            self.add_remove_elements.check_box(item)
        if len(self.add_remove_elements.get_checked_list()) == 2:
            print("TEST PASSED")
        else:
            print("TEST FAILED")

    def test_disable_all_checkboxes(self):
        checked = self.add_remove_elements.get_checked_list()
        for item in checked:
            self.add_remove_elements.check_box(item)
        if len(self.add_remove_elements.get_unchecked_list()) == 2:
            print("TEST PASSED")
        else:
            print("TEST FAILED")

    def run_tests(self):
        try:
            self.test_enable_all_checkboxes()
            self.test_disable_all_checkboxes()
        finally:
            self.driver.close()


if __name__ == "__main__":
    temp = TestCheckboxes()
    temp.run_tests()
