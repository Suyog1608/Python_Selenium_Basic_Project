import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:100")
    yield driver

    driver.quit()


@pytest.fixture
def headless_browser():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:100")
    yield driver
    driver.quit()
