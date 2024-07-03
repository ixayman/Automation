from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()


driver.get("https://www.google.com")

time.sleep(3)
search_input = driver.find_element(By.NAME, 'q')


search_input.send_keys("Python programming")
search_input.send_keys(Keys.ENTER)
time.sleep(3)
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()
driver.quit()
