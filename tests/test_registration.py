from helpers.locators import *
from helpers.generate_data import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.urls import *

def test_success_registration(driver):
    # Тест успешная регистрация
    # Arrange
    name, email, password = generate_registration_data()

    # Act
    driver.get(REG_URL)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(REG_BUTTON))
    driver.find_element(*REG_NAME).send_keys(name)
    driver.find_element(*REG_EMAIL).send_keys(email)
    driver.find_element(*REG_PASS).send_keys(password)
    driver.find_element(*REG_BUTTON).click()

    # Assert
    assert WebDriverWait(driver, 10).until(expected_conditions.url_contains(LOGIN_URL))



def test_error_short_password(driver):
    #     Тест ошибки при коротком пароле
    # Arrange
    name, email, _ = generate_registration_data()

    # Act
    driver.get(REG_URL)
    driver.find_element(*REG_NAME).send_keys(name)
    driver.find_element(*REG_EMAIL).send_keys(email)
    driver.find_element(*REG_PASS).send_keys("888")
    driver.find_element(*REG_BUTTON).click()

    # Assert
    error_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(REG_ERROR))
    assert error_element.is_displayed
    