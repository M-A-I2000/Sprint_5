from selenium.webdriver.common.by import By

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input[contains(@name, 'name')]")
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input[contains(@name, 'name')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@name, 'Пароль')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//a[text() = 'Войти']")
