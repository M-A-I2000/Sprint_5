import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from locators.registration_locator import RegistrationLocators
from curl import *

def test_successful_registration_with_valid_data(driver, valid_name, valid_email, valid_password): #тесты успешной регистрации
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.login(valid_name, valid_email, valid_password)

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/register')

    assert BASE_URL in driver.current_url


@pytest.mark.parametrize(
            'wrong_name, wrong_email, wrong_password', 
            [
                ['','test@yandex.ru','qwerty'], 
                ['Иван', 'test-yandex.ru', 'qwerty123'],
                ['Иван-Иванов', 'test@yandex.ru', '12345']
            ]
    )
def test_registration_fails_with_wrong_data(driver, wrong_name, wrong_email, wrong_password): #тесты неуспешной регистрации
    page = RegistrationPage(driver)
    page.open_registration_page()
    page.login(wrong_name, wrong_email, wrong_password)

    assert driver.current_url == REGISTER_URL