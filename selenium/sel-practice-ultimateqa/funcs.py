from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def open_browser():
    driver = webdriver.Firefox()
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    time.sleep(2)
    return driver


def click_me_button():
    driver = open_browser()
    button = driver.find_element(By.XPATH, "//a[contains(text(),'Click Me')]")
    button.click()
    time.sleep(2)
    current_url = driver.current_url
    if "button-success" in current_url:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def go_to_login_page_button():
    driver = open_browser()
    button = driver.find_element(By.XPATH, "//a[contains(text(),'Go to login page')]")
    button.click()
    time.sleep(2)
    current_url = driver.current_url
    if "sign_in" in current_url:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def click_using_id_button():
    driver = open_browser()
    button = driver.find_element(By.ID, "idExample")
    button.click()
    time.sleep(2)
    current_url = driver.current_url
    if "button-success" in current_url:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def radio_buttons():
    driver = open_browser()
    radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='male']")
    radio_button.click()
    if radio_button:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def email_me():
    driver = open_browser()
    name_field = driver.find_element(By.XPATH, "//input[@data-original_id='name']")
    name_field.send_keys("Ayman")
    email_field = driver.find_element(By.XPATH, "//input[@data-original_id='email']")
    email_field.send_keys("hello@ee.com")
    time.sleep(1)
    button = driver.find_element(By.XPATH, "//button[@class='et_pb_contact_submit et_pb_button']")
    button.click()
    time.sleep(1)
    if driver.find_element(By.XPATH, "//div[@class='et-pb-contact-message']"):
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()
