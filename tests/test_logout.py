from helpers.login import *
from helpers.urls import *
from helpers.users import *


def test_logout_from_personal_account_success(driver):
   # Выход по кнопке «Выйти» в личном кабинете
   # Arrange
   driver.get(LOGIN_URL)
   WebDriverWait(driver, 100).until(expected_conditions.url_to_be(LOGIN_URL))
   login(driver, USER_EMAIL, USER_PASS)

   driver.find_element(*ACCOUNT_BUTTON).click()
   WebDriverWait(driver, 100).until(expected_conditions.url_to_be(PROFILE_URL))
   driver.find_element(*LOGOUT_BUTTON).click()
   WebDriverWait(driver, 100).until(expected_conditions.url_to_be(LOGIN_URL))
   # Assert
   assert driver.current_url in LOGIN_URL