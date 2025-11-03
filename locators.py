from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

# Главная страница
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

# Форма регистрации
REG_NAME = (By.XPATH, "//fieldset[1]//input")
REG_EMAIL = (By.XPATH, "//fieldset[2]//input")
REG_PASS = (By.XPATH, "//fieldset[3]//input")
REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
REG_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
REG_LINK = (By.XPATH, "//a[text()= 'Зарегистрироваться']")
LOGIN_LINK = (By.XPATH, "//a[text()= 'Войти']")

# Форма авторизации
LOGIN_EMAIL = (By.XPATH, "//input[@type='text']")
LOGIN_PASS = (By.XPATH, "//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Конструктор
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")