import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import LOGIN_URL
from locators.login_locator import LoginLocators
from valid_data import *
from helpers import *

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.delete_all_cookies()

    yield driver

    driver.delete_all_cookies()
    driver.quit()

@pytest.fixture(scope="function")
def authorized_user(driver):
    driver.delete_all_cookies()
    
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)

    email_field = wait.until(
        EC.presence_of_element_located((LoginLocators.EMAIL_INPUT))
    )
    email_field.send_keys(registration_email)
    password_field = wait.until(
        EC.presence_of_element_located((LoginLocators.PASSWORD_INPUT))
    )
    password_field.send_keys(registration_password)
    login_button = wait.until(
        EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        )
    login_button.click()
    
    wait.until(lambda driver: driver.current_url != LOGIN_URL)

    return driver

@pytest.fixture
def valid_name():
    names = ["Анна", "Иван", "Мария", "Пётр", "Ольга"]
    return random.choice(names)

@pytest.fixture
def valid_email():
    return generate_email()

@pytest.fixture
def valid_password():
    return generate_password()
