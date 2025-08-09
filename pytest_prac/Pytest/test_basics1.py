from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def launchWebsite():
    driver = webdriver.Chrome()
    driver.get("http://localhost:100")
    return driver


def test_Tc01_verifyUrl():
    driver = launchWebsite()
    exp = "vtiger CRM - Commercial Open Source CRM"
    act = driver.title
    assert act == exp
    time.sleep(2)


def test_Tc02_verifyLogo():
    driver = launchWebsite()
    assert driver.find_element(By.CSS_SELECTOR, "img[src*= 'login_left.gif']").is_displayed() == True
    time.sleep(2)


def test_Tc03_verifyLoginWithInvalidCreds():
    driver = launchWebsite()
    driver.find_element(By.CSS_SELECTOR, "input[name='user_name']").send_keys("admin1")
    driver.find_element(By.CSS_SELECTOR, "input[name='user_password']").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "input[name='Login']").click()
    assert driver.find_element(By.XPATH, "//td[contains(text(), 'username and password')]").is_displayed() == True
    time.sleep(2)


@pytest.mark.parametrize("username, pwd", [
    ("admin1", "admin"),
    ("ad1234", "12345"),
    ("admin2", "ad1245")
])
def test_Tc031_verifyLoginWithInvalidCreds(username, pwd):
    driver = launchWebsite()
    driver.find_element(By.CSS_SELECTOR, "input[name='user_name']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[name='user_password']").send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR, "input[name='Login']").click()
    assert driver.find_element(By.XPATH, "//td[contains(text(), 'username and password')]").is_displayed() == True
    time.sleep(2)


def test_Tc04_verifyLoginWithValidCreds():
    driver = launchWebsite()
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    assert driver.find_element(By.XPATH, "//strong[contains(text(), ' admin')]").is_displayed() == True
    time.sleep(2)


def test_Tc05_verifyLogout():
    driver = launchWebsite()
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    driver.find_element(By.XPATH, "//a[text()= 'Logout']").click()
    assert driver.find_element(By.CSS_SELECTOR, "img[src*='login_left']").is_displayed()
    time.sleep(2)