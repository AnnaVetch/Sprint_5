from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.locators import *
from helpers.urls import *
from helpers.users import *


def test_success_login(driver):
    # Вход по кнопке «Войти в аккаунт» на главной
    # Arrange

    # Act
    driver.get(HOST)
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    driver.find_element(*LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*LOGIN_PASS).send_keys(USER_PASS)
    driver.find_element(*LOGIN_BUTTON).click()

    # Assert
    assert WebDriverWait(driver, 100).until(expected_conditions.url_to_be(HOST))


def test_login_account_button(driver):
    # Вход через кнопку «Личный кабинет»
    # Arrange

    driver.get(HOST)
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*LOGIN_PASS).send_keys(USER_PASS)
    driver.find_element(*LOGIN_BUTTON).click()

    # Assert
    assert WebDriverWait(driver, 100).until(expected_conditions.url_to_be(HOST))


def test_login_from_registration_form_success(driver):
    # Вход через кнопку в форме регистрации

    driver.get(REG_URL)
    WebDriverWait(driver, 1000).until(expected_conditions.url_contains(REG_URL))

    driver.find_element(*LOGIN_LINK).click()
    WebDriverWait(driver, 1000).until(expected_conditions.url_contains(LOGIN_URL))

    driver.find_element(*LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*LOGIN_PASS).send_keys(USER_PASS)
    driver.find_element(*LOGIN_BUTTON).click()

    # Assert
    assert WebDriverWait(driver, 1000).until(expected_conditions.url_to_be(HOST))


def test_login_from_recovery_form_success(driver):
    # Вход через кнопку в форме восстановления пароля
    # Arrange

    # Act
    driver.get(RECOVERY_URL)
    WebDriverWait(driver, 1000).until(expected_conditions.url_contains(RECOVERY_URL))

    driver.find_element(*LOGIN_LINK).click()
    WebDriverWait(driver, 1000).until(expected_conditions.url_contains(LOGIN_URL))

    driver.find_element(*LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*LOGIN_PASS).send_keys(USER_PASS)
    driver.find_element(*LOGIN_BUTTON).click()

    # Assert
    assert WebDriverWait(driver, 1000).until(expected_conditions.url_to_be(LOGIN_URL))
