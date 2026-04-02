from selenium.webdriver.common.by import By

class ProfileLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")