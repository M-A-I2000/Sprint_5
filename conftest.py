import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import LOGIN_URL
from valid_data import *

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
        EC.presence_of_element_located((By.XPATH, "//input[contains(@name, 'name')]"))
    )
    email_field.send_keys(registration_email)
    driver.find_element(By.XPATH, "//input[contains(@name, 'Пароль')]").send_keys(registration_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    wait.until(lambda driver: driver.current_url != LOGIN_URL)

    return driver

import string
import random

def generate_email(domain="testsprint5.ru", length=8):
    characters = string.ascii_lowercase + string.digits
    local_part = ''.join(random.choice(characters) for _ in range(length))
    return f"{local_part}@{domain}"

def generate_password(length=12):
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)

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
