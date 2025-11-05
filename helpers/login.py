from helpers.locators import *
from helpers.urls import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def login(driver, email, password):
    #Улита для аторизации
    driver.find_element(*LOGIN_EMAIL).send_keys(email)
    driver.find_element(*LOGIN_PASS).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 100).until(expected_conditions.url_to_be(HOST))
    