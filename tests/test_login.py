import pytest
from pages.login_page import LoginPage
from curl import *
from valid_data import *

class TestLoginPage:

    def test_success_login(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(registration_email, registration_password)
        page.successful_login()

        assert page.is_base_url_contains()

    def test_login_via_button_on_main_page(self, driver): #вход по кнопке «Войти в аккаунт» на главной
        driver.get(BASE_URL)
        page = LoginPage(driver)
        page.find_account_login_button()
        page.login(registration_email, registration_password)
        page.successful_login()

        assert page.is_order_button_visible()


    def test_login_via_link_in_profile_menu(self, driver): #вход через кнопку «Личный кабинет»
        driver.get(BASE_URL)
        page = LoginPage(driver)
        page.find_personal_account_login_button()
        page.login(registration_email, registration_password)
        page.successful_login()

        assert page.is_order_button_visible()


    def test_navigate_to_login_from_registration(self, driver): #вход через кнопку в форме регистрации
        driver.get(REGISTER_URL)
        page = LoginPage(driver)
        page.find_login_button_on_registration_page()
        page.login(registration_email, registration_password)
        page.successful_login()
        
        assert page.is_order_button_visible()


    def test_navigate_to_login_from_recovery(self, driver): #вход через кнопку в форме восстановления пароля
        driver.get(FORGOT_PASSWORD_URL)
        page = LoginPage(driver)
        page.find_login_button_on_recovery_page()
        page.login(registration_email, registration_password)
        page.successful_login
        
        assert page.is_order_button_visible()



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
    def test_invalid_login(self, driver, wrong_email, wrong_password):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(wrong_email, wrong_password)

        assert page.is_on_login_page()

