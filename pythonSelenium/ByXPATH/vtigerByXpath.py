import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:100")

driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin")
driver.find_element(By.XPATH, "//select[@name='login_theme']").send_keys("orange")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(1)

driver.find_element(By.XPATH, "//a[text()='New Lead']").click()

driver.find_element(By.XPATH, "//select[@name='salutationtype']").send_keys("Mr.")
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Suyog")
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Gadhave")
driver.find_element(By.XPATH, "//input[@name='company']").send_keys("Infor")
driver.find_element(By.XPATH, "//input[@name='designation']").send_keys("Associate QA")

driver.find_element(By.XPATH, "//select[@name='leadsource']").send_keys("Employee")
driver.find_element(By.XPATH, "//select[@name='industry']").send_keys("Engineering")
driver.find_element(By.XPATH, "//input[@name='annualrevenue']").send_keys("1000")
driver.find_element(By.XPATH, "//input[@name='noofemployees']").send_keys("40")
driver.find_element(By.XPATH, "//input[@name='yahooid']").send_keys("test1234@yahoo.com")
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("9834749465")
driver.find_element(By.XPATH, "//input[@name='mobile']").send_keys("0987654321")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("gadhavesuyog@gmail.com")
driver.find_element(By.XPATH, "//input[@name='website']").send_keys("http://localhost:100")
driver.find_element(By.XPATH, "//select[@name='leadstatus']").send_keys("Qualified")
driver.find_element(By.XPATH, "//select[@name='rating']").send_keys("Active")
driver.find_element(By.XPATH, "//input[@value='T']").click()
driver.find_element(By.XPATH, "//textarea[@name='lane']").send_keys("Lohegaon")
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Pune")
driver.find_element(By.XPATH, "//input[@name='state']").send_keys("Maharashtra")
driver.find_element(By.XPATH, "//input[@name='code']").send_keys("411047")
driver.find_element(By.XPATH, "//input[@name='country']").send_keys("India")
driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys(
    "The Sunrise Valley is a picturesque destination nestled in the "
    "heart of the mountains, known for its breathtaking views, "
    "serene atmosphere, and vibrant wildlife. Visitors can enjoy a "
    "variety of outdoor activities such as hiking, bird-watching, "
    "and camping, all while surrounded by lush forests and "
    "cascading waterfalls. The valley’s charm lies in its untouched "
    "natural beauty and the peaceful rhythm of life it offers, "
    "making it a perfect getaway for nature lovers and adventure "
    "seekers alike.")
time.sleep(1)

driver.find_elements(By.NAME, "button")[2].click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='Duplicate']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//select[@name='salutationtype']").send_keys("Ms.")
driver.find_element(By.XPATH, "//input[@name='firstname']").clear()
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Shweta")
driver.find_element(By.XPATH, "//input[@name='lastname']").clear()
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Zarekar")
driver.find_element(By.XPATH, "//input[@name='designation']").clear()
driver.find_element(By.XPATH, "//input[@name='designation']").send_keys("QA Madam")
driver.find_element(By.XPATH, "//input[@name='phone']").clear()
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("8080184052")
driver.find_element(By.XPATH, "//input[@name='email']").clear()
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("shwetakhobare123@gmail.com")
driver.find_element(By.XPATH, "//textarea[@name='lane']").clear()
driver.find_element(By.XPATH, "//textarea[@name='lane']").send_keys("Hinjewadi")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='code']").clear()
driver.find_element(By.XPATH, "//input[@name='code']").send_keys("411057")

driver.find_elements(By.XPATH, "//input[@type='submit']")[2].click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[text()='Leads']").click()
driver.find_elements(By.XPATH, "//input[@name='firstname']")[1].send_keys("Suyog")
driver.find_elements(By.XPATH, "//input[@name='lastname']")[1].send_keys("Gadhave")
driver.find_element(By.XPATH, "//input[@name='company']").send_keys("Infor")

driver.find_elements(By.XPATH, "//input[@value='Search']")[1].click()

driver.find_element(By.XPATH, "//input[@name='selectall']").click()

driver.find_element(By.XPATH, "//input[@type='submit' and @value='Delete']").click()
time.sleep(1)

driver.find_elements(By.XPATH, "//input[@name='firstname']")[1].send_keys("Shweta")
driver.find_elements(By.XPATH, "//input[@name='lastname']")[1].send_keys("Zarekar")
driver.find_element(By.XPATH, "//input[@name='company']").send_keys("Infor")

driver.find_elements(By.XPATH, "//input[@value='Search']")[1].click()

driver.find_element(By.XPATH, "//input[@name='selectall']").click()
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Delete']").click()

driver.find_element(By.XPATH, "//a[text()='Logout']").click()

time.sleep(5)
