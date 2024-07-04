from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from sel.POM.herokuapp2.infra.browser_wrapper import BrowserWrapper
from sel.POM.herokuapp2.logic.add_remove_elements_page import AddRemoveElements


def get_driver():
    browser_wrapper = BrowserWrapper()
    driver = browser_wrapper.get_driver('https://the-internet.herokuapp.com/add_remove_elements/')
    return driver


class TestAddRemoveElements:

    def test_Add_element(self):
        driver = get_driver()
        add_remove_elements = AddRemoveElements(driver)
        add_remove_elements.click_add_element()
        if len(add_remove_elements.get_delete_buttons_list()) == 1:
            print("TEST PASS")
        else:
            print("TEST FAILED")
        driver.quit()

    def test_Add_multiple_elements(self, number):
        driver = get_driver()
        add_remove_elements = AddRemoveElements(driver)
        add_remove_elements.add_multiple_elements(number)
        if len(add_remove_elements.get_delete_buttons_list()) == number:
            print("TEST PASS")
        else:
            print("TEST FAILED")
        driver.quit()

    def test_delete_buttons(self):
        driver = get_driver()
        add_remove_elements = AddRemoveElements(driver)
        add_remove_elements.add_multiple_elements(7)
        add_remove_elements.click_delete_button()
        print("TEST PASS")
        driver.quit()


if __name__ == "__main__":
    temp = TestAddRemoveElements()
    temp.test_Add_element()
    temp.test_Add_multiple_elements(10)
    temp.test_delete_buttons()
