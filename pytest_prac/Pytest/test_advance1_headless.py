from selenium.webdriver.common.by import By
import pytest
import time


def test_tc08_VerifyLogoAdvance(headless_browser):
    assert headless_browser.find_element(By.CSS_SELECTOR, "img[src*= 'login_left.gif']").is_displayed() == True
    time.sleep(2)


def test_Tc09_verifyLoginWithInvalidCreds(headless_browser):
    driver = headless_browser
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
def test_Tc091_verifyLoginWithInvalidCreds(username, pwd, headless_browser):
    driver = headless_browser
    driver.find_element(By.CSS_SELECTOR, "input[name='user_name']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[name='user_password']").send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR, "input[name='Login']").click()
    assert driver.find_element(By.XPATH, "//td[contains(text(), 'username and password')]").is_displayed() == True
    time.sleep(2)


def test_Tc010_verifyLoginWithValidCreds(headless_browser):
    driver = headless_browser
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    assert driver.find_element(By.XPATH, "//strong[contains(text(), ' admin')]").is_displayed() == True
    time.sleep(2)


def test_Tc011_verifyLogout(headless_browser):
    driver = headless_browser
    driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='Login']").click()
    driver.find_element(By.XPATH, "//a[text()= 'Logout']").click()
    assert driver.find_element(By.CSS_SELECTOR, "img[src*='login_left']").is_displayed()
    time.sleep(2)