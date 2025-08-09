from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_tc06_verifyPage(browser):
    exp = "vtiger CRM - Commercial Open Source CRM"
    act = browser.title
    assert exp == act
    time.sleep(2)
