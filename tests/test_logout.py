from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locator import ProfileLocators
from locators.login_locator import LoginLocators
from curl import LOGIN_URL

def test_logout_button_click_shows_login_form(authorized_user):
    driver = authorized_user
    wait = WebDriverWait(driver, 10)

    from locators.base_locator import BaseLocators
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    login_button.click()

    logout_button = wait.until(
        EC.element_to_be_clickable((ProfileLocators.LOGOUT_BUTTON))
    )
    logout_button.click()

    wait.until(lambda driver: driver.current_url == LOGIN_URL)

    login_button = wait.until(
        EC.visibility_of_element_located((LoginLocators.LOGIN_BUTTON))
    )
    
    assert login_button.is_displayed()