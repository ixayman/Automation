from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

def click_me_button():
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

    button = driver.find_element(By.XPATH, "//a[contains(text(),'Click Me')]")
    button.click()
    driver.close()
