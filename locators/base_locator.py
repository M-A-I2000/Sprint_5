from selenium.webdriver.common.by import By

class BaseLocators:
    LOGO_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
    ACCOUNT_LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
