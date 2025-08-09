import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:100")

driver.find_element(By.NAME, "user_name").send_keys("admin")
driver.find_element(By.NAME, "user_password").send_keys("admin")
driver.find_element(By.NAME, "login_theme").send_keys("blue")
driver.find_element(By.NAME, "Login").click()

driver.find_element(By.LINK_TEXT, "New Lead").click()

driver.find_element(By.NAME, "salutationtype").send_keys("Mr.")
driver.find_element(By.NAME, "firstname").send_keys("Suyog")
driver.find_element(By.NAME, "lastname").send_keys("Gadhave")
driver.find_element(By.NAME, "company").send_keys("Infor")

elms = driver.find_elements(By.NAME, "assigntype")
elms[1].click()
time.sleep(1)

btns = driver.find_elements(By.NAME, "button")
btns[2].click()
time.sleep(1)

driver.find_element(By.NAME, "Edit").click()
time.sleep(1)

driver.find_element(By.NAME, "lastname").clear()
driver.find_element(By.NAME, "lastname").send_keys("hello")

driver.find_element(By.LINK_TEXT, "Leads").click()

driver.find_elements(By.NAME, "lastname")[1].send_keys("Gadhave")

driver.find_elements(By.NAME,"button")[1].click()

time.sleep(2)

driver.find_element(By.NAME,"selectall").click()
driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[1]/td[2]/table[5]/tbody/tr/td[3]/table/tbody/tr/td[1]/input[1]").click()

driver.find_element(By.LINK_TEXT,"Logout").click()

time.sleep(2)