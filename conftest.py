import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Фикстура для запуска браузера Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options)

    driver.maximize_window()
    yield driver
    driver.quit()
