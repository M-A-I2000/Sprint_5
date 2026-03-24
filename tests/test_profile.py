from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locator import ProfileLocators
from locators.login_locator import LoginLocators
from curl import *

def test_click_personal_account_button_opens_personal_account_page(authorized_user): #переход в ЛК
    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    login_button.click()

    logout_button = wait.until(
        EC.visibility_of_element_located((ProfileLocators.LOGOUT_BUTTON))
    )

    assert logout_button.is_displayed()


def test_click_constructor_button_opens_constructor_page(authorized_user): #переход в Конструктор из ЛК
    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    login_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/account/profile')

    constructor_button = wait.until(
        EC.element_to_be_clickable(ProfileLocators.CONSTRUCTOR_BUTTON)
    )
    constructor_button.click()

    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)


def test_logo_click_navigates_to_homepage(authorized_user): #переход на главную страницу по клику на лого
    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    login_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != BASE_URL + '/account/profile')

    logo_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.LOGO_BUTTON)
    )
    logo_button.click()

    assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)