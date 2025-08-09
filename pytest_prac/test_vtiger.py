from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_tc06_verifyVtiger(browser):
    assert browser.find_element(By.XPATH, "//img[@src='include/images/vtiger-crm.gif']").is_displayed()
    time.sleep(5)
