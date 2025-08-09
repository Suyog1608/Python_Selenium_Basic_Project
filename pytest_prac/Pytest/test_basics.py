from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


# def add(a, b):
#     return a + b
#
#
# def test_add():
#     assert add(2, 4) == 6

# def test_add1():
#     assert add(2,5) == 4

def launchWebsite():
    driver = webdriver.Chrome()
    driver.get("http://localhost:100")
    return driver


def test_tc01_verifyURL():
    # driver = webdriver.Chrome()
    # driver.get("http://localhost:100")
    driver = launchWebsite()
    exp = "vtiger CRM - Commercial Open Source CRM"
    act = driver.title
    assert exp == act


def test_tc02_verifyLogo():
    # driver.get("http://localhost:100")
    driver = launchWebsite()
    assert driver.find_element(By.XPATH, "//img[@src='include/images/vtiger-crm.gif']").is_displayed() == True


def test_tc03_verifyLoginWithIncorrectCreds():
    # driver = webdriver.Chrome()
    # driver.get("http://localhost:100")
    driver = launchWebsite()
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("test")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("1234")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    assert driver.find_element(By.XPATH,
                               "//*[contains(text(),'You must specify a valid username and password.')]").is_displayed() == True


def test_tc04_verifyLogin():
    # driver = webdriver.Chrome()
    # driver.get("http://localhost:100")
    driver = launchWebsite()
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed() == True


time.sleep(5)


@pytest.mark.parametrize("userid, pwd", [
    ("admin1", "pwd1"),
    ("admin2", "pwd2"),
    ("test12", "pwd")
])
def test_tc05_verifyLoginWithIncorrectCreds(userid, pwd):  # Testing Login using different Credentials
    driver = launchWebsite()
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys(userid)
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys(pwd)
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    assert driver.find_element(By.XPATH,
                               "//*[contains(text(),'You must specify a valid username and password.')]").is_displayed() == True
