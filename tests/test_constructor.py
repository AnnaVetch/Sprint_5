from helpers.urls import *
from helpers.locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_constructor_section_buns_success(driver):
    # Переход из раздела "Конструктор" в раздел "Булки"
    # Arrange
    driver.get(HOST)
    WebDriverWait(driver, 1000).until(expected_conditions.url_to_be(HOST))

    #Act
    driver.find_element(*SAUCES_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SAUCES_TAB).get_attribute("class"))
    driver.find_element(*BUNS_TAB).click()
    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in d.find_element(*BUNS_TAB).get_attribute("class"))

    #Assert
    assert "tab_tab_type_current" in driver.find_element(*BUNS_TAB).get_attribute("class")

def test_constructor_section_sauces_success(driver):
    # Переход из раздела "Конструктор" в раздел "Соусы"
    # Arrange
    driver.get(HOST)
    WebDriverWait(driver, 1000).until(expected_conditions.url_to_be(HOST))

    # Act
    driver.find_element(*SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SAUCES_TAB).get_attribute("class"))

    #Assert
    assert "tab_tab_type_current" in driver.find_element(*SAUCES_TAB).get_attribute("class")


def test_constructor_section_fillings_success(driver):
    # Переход из раздела "Конструктор" в раздел "Начинки"
    # Arrange
    driver.get(HOST)
    WebDriverWait(driver, 1000).until(expected_conditions.url_to_be(HOST))

    # Act
    driver.find_element(*FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current" in d.find_element(*FILLINGS_TAB).get_attribute("class"))


    #Assert
    assert "tab_tab_type_current" in driver.find_element(*FILLINGS_TAB).get_attribute("class")
    