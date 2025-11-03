import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Фикстура для запуска браузера Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options)

    driver.maximize_window()
    yield driver
    driver.quit()