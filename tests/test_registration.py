import pytest
from pages.registration_page import RegistrationPage
from curl import *

class TestRegistrationPage:

    def test_successful_registration_with_valid_data(self, driver, valid_name, valid_email, valid_password): #тесты успешной регистрации
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.login(valid_name, valid_email, valid_password)
        page.successful_registration()

        assert page.is_base_url_contains()


    @pytest.mark.parametrize(
                'wrong_name, wrong_email, wrong_password', 
                [
                    ['','test@yandex.ru','qwerty'], 
                    ['Иван', 'test-yandex.ru', 'qwerty123'],
                    ['Иван-Иванов', 'test@yandex.ru', '12345']
                ]
        )
    def test_registration_fails_with_wrong_data(self, driver, wrong_name, wrong_email, wrong_password): #тесты неуспешной регистрации
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.login(wrong_name, wrong_email, wrong_password)

        assert page.is_on_registration_page()
        