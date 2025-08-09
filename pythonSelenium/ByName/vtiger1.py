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
driver.find_element(By.NAME, "designation").send_keys("Associate Quality Assurance Analyst")
driver.find_element(By.NAME, "leadsource").send_keys("Employee")
driver.find_element(By.NAME, "industry").send_keys("Engineering")
driver.find_element(By.NAME, "noofemployees").send_keys("50")
driver.find_element(By.NAME, "phone").send_keys("9834749465")
driver.find_element(By.NAME, "mobile").send_keys("2468135709")
driver.find_element(By.NAME, "email").send_keys("gadhavesuyog@gmail.com")
driver.find_element(By.NAME, "website").send_keys("http://localhost:100/")
driver.find_element(By.NAME, "leadstatus").send_keys("Qualified")
driver.find_element(By.NAME, "rating").send_keys("Active")
time.sleep(1)
driver.find_elements(By.NAME, "assigntype")[1].click()

driver.find_element(By.NAME, "lane").send_keys("Lohegaon")
driver.find_elements(By.NAME, "city")[1].send_keys("Pune")
time.sleep(1)
driver.find_element(By.NAME, "state").send_keys("Maharashtra")
driver.find_element(By.NAME, "code").send_keys("411047")
driver.find_element(By.NAME, "country").send_keys("India")
driver.find_element(By.NAME, "description").send_keys("The Sunrise Valley is a picturesque destination nestled in the "
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

time.sleep(2)

driver.find_element(By.NAME, "Duplicate").click()

driver.find_element(By.NAME, "salutationtype").send_keys("Ms.")
driver.find_element(By.NAME, "firstname").clear()
driver.find_element(By.NAME, "firstname").send_keys("Shweta")
driver.find_element(By.NAME, "lastname").clear()
driver.find_element(By.NAME, "lastname").send_keys("Zarekar")
driver.find_element(By.NAME, "phone").clear()
driver.find_element(By.NAME, "phone").send_keys("8080184052")
driver.find_elements(By.NAME, "assigntype")[1].click()
driver.find_element(By.NAME, "lane").clear()
driver.find_element(By.NAME, "lane").send_keys("Hinjewadi")
time.sleep(1)
driver.find_elements(By.NAME, "city")[1].clear()
driver.find_elements(By.NAME, "city")[1].send_keys("Pimpri-Chinchwad")
driver.find_element(By.NAME, "code").clear()
driver.find_element(By.NAME, "code").send_keys("411057")

driver.find_elements(By.NAME, "button")[2].click()

time.sleep(1)

driver.find_element(By.LINK_TEXT, "Leads").click()

driver.find_elements(By.NAME, "firstname")[1].send_keys("Suyog")
driver.find_elements(By.NAME, "lastname")[1].send_keys("Gadhave")
driver.find_elements(By.NAME, "company")[1].send_keys("Infor")
time.sleep(1)
driver.find_element(By.XPATH,
                    "/html/body/table[2]/tbody/tr[1]/td[2]/table[3]/tbody/tr/td/table/tbody/tr[1]/td[7]/input[7]").click()
time.sleep(1)

driver.find_element(By.NAME, "selectall").click()
driver.find_element(By.XPATH,
                    "/html/body/table[2]/tbody/tr[1]/td[2]/table[5]/tbody/tr/td[3]/table/tbody/tr/td[1]/input[1]").click()

time.sleep(2)

driver.find_elements(By.NAME, "firstname")[1].send_keys("Shweta")
driver.find_elements(By.NAME, "lastname")[1].send_keys("Zarekar")
driver.find_elements(By.NAME, "company")[1].send_keys("Infor")
time.sleep(1)
driver.find_element(By.XPATH,
                    "/html/body/table[2]/tbody/tr[1]/td[2]/table[3]/tbody/tr/td/table/tbody/tr[1]/td[7]/input[7]").click()

driver.find_element(By.NAME, "selectall").click()
driver.find_element(By.XPATH,
                    "/html/body/table[2]/tbody/tr[1]/td[2]/table[5]/tbody/tr/td[3]/table/tbody/tr/td[1]/input[1]").click()

time.sleep(2)

driver.find_elements(By.NAME, "firstname")[0].send_keys("Suyog")
driver.find_elements(By.NAME, "lastname")[0].send_keys("Gadhave")
driver.find_elements(By.NAME, "company")[0].send_keys("Infor")
driver.find_element(By.NAME, "phone").send_keys("9834749465")
driver.find_element(By.NAME, "email").send_keys("gadhavesuyog@gmail.com")
time.sleep(1)
driver.find_elements(By.NAME, "button")[0].click()

time.sleep(1)

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Calendar").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Activities").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Leads").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Accounts").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Contacts").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Potentials").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Products").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Logout").click()

time.sleep(2)
