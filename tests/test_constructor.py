from helpers.urls import *
from helpers.locators import *

def test_constructor_section_buns_success(driver):
    # Переход из раздела "Конструктор" в раздел "Булки"
    # Arrange
    driver.get(HOST)

    #Act
    driver.find_element(*SAUCES_TAB).click()
    driver.find_element(*BUNS_TAB).click()
    buns_text = driver.find_element(*BUNS_TAB).text
    bun_displayed = driver.find_element(*BUNS_TAB).is_displayed()

    #Assert
    assert buns_text == 'Булки' and bun_displayed

def test_constructor_section_sauces_success(driver):
    # Переход из раздела "Конструктор" в раздел "Соусы"
    # Arrange
    driver.get(HOST)

    # Act
    driver.find_element(*SAUCES_TAB).click()
    sauces_text = driver.find_element(*SAUCES_TAB).text
    sauces_displayed = driver.find_element(*SAUCES_TAB).is_displayed()

    #Assert
    assert sauces_text == 'Соусы' and sauces_displayed


def test_constructor_section_fillings_success(driver):
    # Переход из раздела "Конструктор" в раздел "Начинки"
    # Arrange
    driver.get(HOST)

    # Act
    driver.find_element(*FILLINGS_TAB).click()
    fillings_text = driver.find_element(*FILLINGS_TAB).text
    fillings_displayed = driver.find_element(*FILLINGS_TAB).is_displayed()

    #Assert
    assert fillings_text == 'Начинки' and fillings_displayed