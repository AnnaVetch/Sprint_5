from helpers.login import *
from urls import *
from users import *


def test_success_login(driver):
    # Вход по клику на кнопку «Личный кабинет»

    # Arrange

    # Act
    driver.get(HOST)
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL).send_keys(USER_EMAIL)
    driver.find_element(*LOGIN_PASS).send_keys(USER_PASS)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(HOST))

    # Assert
    assert driver.current_url in HOST


def test_logout_from_personal_account_to_constructor_by_click_logo_success(driver):
    # Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    # Arrange
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(LOGIN_URL))
    login(driver, USER_EMAIL, USER_PASS)

    # Act
    driver.find_element(*ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(PROFILE_URL))
    driver.find_element(*LOGO_BUTTON).click()

    # Assert
    assert driver.current_url in HOST


def test_logout_from_personal_account_to_constructor_by_click_constructor_button_success(driver):
    # Переход из личного кабинета в конструктор по клику на кнопку "Конструктор"
    # Arrange
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(LOGIN_URL))
    login(driver, USER_EMAIL, USER_PASS)

    driver.find_element(*ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(PROFILE_URL))
    driver.find_element(*CONSTRUCTOR_BUTTON).click()

    # Assert
    assert driver.current_url in HOST
