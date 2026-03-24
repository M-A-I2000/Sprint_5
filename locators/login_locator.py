from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[contains(@name, 'name')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@name, 'Пароль')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    WRONG_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']")