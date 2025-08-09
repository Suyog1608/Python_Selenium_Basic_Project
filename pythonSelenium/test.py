import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("gadhavesuyog@gmail.com")

driver.find_element(By.NAME, "pass").send_keys("suyog1234")

driver.find_element(By.NAME, "login").click()

time.sleep(5)