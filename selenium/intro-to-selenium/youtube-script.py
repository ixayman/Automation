from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.youtube.com")

search_input = driver.find_element(By.XPATH, '//input[@id="search"]')

search_input.send_keys("hello")
search_input.send_keys(Keys.ENTER)

driver.quit()
