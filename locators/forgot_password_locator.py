from selenium.webdriver.common.by import By

class RestoreLocators:
    EMAIL_INPUT = (By.XPATH, "//input[contains(@class, 'input')]")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Войти')]")
