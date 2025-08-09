import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")

driver.find_element(By.ID, "username").send_keys("gadhavesuyog@gmail.com")
driver.find_element(By.ID, 'password').send_keys("test@1234")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

driver.quit()