import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import LOGIN_URL
from pages.login_page import LoginPage
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

    page = LoginPage(driver)
    page.login_with_valid_data()

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
