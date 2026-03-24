import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from locators.login_locator import LoginLocators
from curl import *
from valid_data import *


def test_success_login(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login(registration_email, registration_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/login')

    assert BASE_URL in driver.current_url

def test_login_via_button_on_main_page(driver): #вход по кнопке «Войти в аккаунт» на главной
    driver.get(BASE_URL)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.ACCOUNT_LOGIN_BUTTON)
    )
    login_button.click()

    wait.until(
        EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
    )

    page = LoginPage(driver)
    page.login(registration_email, registration_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/login')

    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)


def test_login_via_link_in_profile_menu(driver): #вход через кнопку «Личный кабинет»
    driver.get(BASE_URL)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    login_button.click()

    wait.until(
        EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
    )

    page = LoginPage(driver)
    page.login(registration_email, registration_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/login')

    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)


def test_navigate_to_login_from_registration(driver): #вход через кнопку в форме регистрации
    driver.get(REGISTER_URL)

    from locators.registration_locator import RegistrationLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(RegistrationLocators.LOGIN_BUTTON)
    )
    login_button.click()

    wait.until(
        EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
    )

    page = LoginPage(driver)
    page.login(registration_email, registration_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/login')
    
    from locators.base_locator import BaseLocators
    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)


def test_navigate_to_login_from_recovery(driver): #вход через кнопку в форме восстановления пароля
    driver.get(FORGOT_PASSWORD_URL)

    from locators.forgot_password_locator import RestoreLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(RestoreLocators.LOGIN_BUTTON)
    )
    login_button.click()

    wait.until(
        EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
    )

    page = LoginPage(driver)
    page.login(registration_email, registration_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/login')
    
    from locators.base_locator import BaseLocators
    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)



@pytest.mark.parametrize(
            'wrong_email, wrong_password', 
            [
                ['AlexandrMorozov40890@yandex.ru','qwerty12'], 
                ['AlexandrMorozov408902yandex.ru', 'qwerty123'],
                ['AlexandrMorozov40890@yandex.ru', 'q'],
                ['AlexandrMorozov40890@yandex.ru', 'qw'],
                ['AlexandrMorozov40890@yandex.ru', 'qwer'],
                ['AlexandrMorozov40890@yandex.ru', 'qwert'],
                ['AlexandrMorozov40890@yandex.ru', 'qwerty']
            ]
    )
def test_invalid_login(driver, wrong_email, wrong_password):
    page = LoginPage(driver)
    page.open_login_page()
    page.login(wrong_email, wrong_password)

    assert driver.current_url == LOGIN_URL

