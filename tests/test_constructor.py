from helpers.urls import *
from helpers.locators import *

def test_constructor_section_buns_success(driver):
    # Переход из раздела "Конструктор" в раздел "Булки"
    # Arrange
    driver.get(HOST)

    #Act
    driver.find_element(*SAUCES_TAB).click()
    driver.find_element(*BUNS_TAB).click()

    #Assert
    assert "tab_tab_type_current" in driver.find_element(*BUNS_TAB).get_attribute("class")

def test_constructor_section_sauces_success(driver):
    # Переход из раздела "Конструктор" в раздел "Соусы"
    # Arrange
    driver.get(HOST)

    # Act
    driver.find_element(*SAUCES_TAB).click()

    #Assert
    assert "tab_tab_type_current" in driver.find_element(*SAUCES_TAB).get_attribute("class")


def test_constructor_section_fillings_success(driver):
    # Переход из раздела "Конструктор" в раздел "Начинки"
    # Arrange
    driver.get(HOST)

    # Act
    driver.find_element(*FILLINGS_TAB).click()

    #Assert
    assert "tab_tab_type_current" in driver.find_element(*FILLINGS_TAB).get_attribute("class")
    