from selenium.webdriver.common.by import By

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]//following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@name, 'Пароль')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//a[text() = 'Войти']")
