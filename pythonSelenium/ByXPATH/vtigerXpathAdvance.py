import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:100/")

driver.find_element(By.XPATH, "//input[contains(@name, '_name')]").send_keys("admin")
driver.find_element(By.XPATH, "//input[substring(@name,4) ='r_password']").send_keys("admin")
driver.find_element(By.XPATH, "//select[@name='login_theme']").send_keys("blue")
driver.find_element(By.XPATH, "//input[@type='submit' and @name='Login']").click()

time.sleep(1)

driver.find_element(By.XPATH, "//a[text()='New Lead']").click()

driver.find_element(By.XPATH, "//select[contains(@name, 'salutation')]").send_keys("Mr.")
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Suyog")
driver.find_element(By.XPATH, "//input[@type='text' and @name='lastname']").send_keys("Gadhave")
driver.find_element(By.XPATH, "//input[@name='company']").send_keys("Infor")
driver.find_element(By.XPATH, "//td[text()='Company:']/following::input[1]").send_keys("Associate QA")
driver.find_element(By.XPATH, "//td[text()='Lead Source:']/following::select[1]").send_keys("Partner")
driver.find_element(By.XPATH, "//input[@name = 'annualrevenue']").send_keys("1200")
driver.find_element(By.XPATH, "//td[text()='Yahoo Id:']/following::input[1]").send_keys("test@yahoo.com")
driver.find_element(By.XPATH, "//input[@name='company']/preceding::input[1]").send_keys("9834749465")
driver.find_element(By.XPATH, "//input[@name = 'website']/preceding::input[1]").send_keys("gadhavesuyog@gmail.com")
driver.find_element(By.XPATH, "//td[contains(text(), 'Rating:')]/following::select[1]").send_keys("Acquired")
driver.find_element(By.XPATH, "//tr[8]/following-sibling::tr[1]/td[4]/input[2]").click()

driver.find_element(By.XPATH, "//input[@name='code']/preceding::textarea[@name='lane']").send_keys("Lohegaon-Wagholi")
driver.find_element(By.XPATH, "//form//table//tr[3]//input[@name='city']").send_keys("Pune")
driver.find_element(By.XPATH, "//form//table//tr[4]//input[@name='state']").send_keys("Maharashtra")
driver.find_element(By.XPATH, "//table[4]//descendant::input[@name='code']").send_keys("411047")
driver.find_element(By.XPATH, "//table[4]//descendant::input[3]").send_keys("India")

driver.find_element(By.XPATH, "//table[5]//descendant::textarea").send_keys(
    "The Sunrise Valley is a picturesque destination nestled in the "
    "heart of the mountains, known for its breathtaking views, "
    "serene atmosphere, and vibrant wildlife. Visitors can enjoy a "
    "variety of outdoor activities such as hiking, bird-watching, "
    "and camping, all while surrounded by lush forests and "
    "cascading waterfalls. The valley’s charm lies in its untouched "
    "natural beauty and the peaceful rhythm of life it offers, "
    "making it a perfect getaway for nature lovers and adventure "
    "seekers alike.")

driver.find_element(By.XPATH, "//table[6]//descendant::input[1]").click()

driver.find_element(By.XPATH, "//table//descendant::a[contains(text(),'New Account')]").click()
driver.find_element(By.XPATH, "//input[contains(@name, 'account')]").send_keys("Savings Account")
driver.find_element(By.XPATH, "//input[contains(@name, 'l_city')]").send_keys("Pune")
driver.find_element(By.XPATH, "//table[6]//descendant::input[1]").click()

# driver.find_element(By.XPATH, "//table//descendant::a[contains(text(),'New Potential')]").click()
# driver.find_element(By.XPATH, "//form//descendant::input[@name='potentialname']").send_keys("Suyog Gadhave")
# driver.find_element(By.XPATH, "//table[2]//td[2]//td[2]//input[3]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//a[contains(@onclick, 'Savings Account')]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//table[5]//descendant::input[1]").click()


time.sleep(2)
