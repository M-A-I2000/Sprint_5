from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_locator import LoginLocators
from locators.base_locator import BaseLocators
from locators.registration_locator import RegistrationLocators
from locators.forgot_password_locator import RestoreLocators
from curl import *

class LoginPage(BasePage):

    def open_login_page(self):
        self.open(LOGIN_URL)

    def login(self, username, password):
        self.type(LoginLocators.EMAIL_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def successful_login(self):
        self.wait.until(lambda driver: driver.current_url != BASE_URL + '/login')

    def find_account_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(BaseLocators.ACCOUNT_LOGIN_BUTTON)
        )
        login_button.click()

        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )

    def find_personal_account_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        login_button.click()

        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )

    def find_login_button_on_registration_page(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(RegistrationLocators.LOGIN_BUTTON)
        )
        login_button.click()

        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )

    def find_login_button_on_recovery_page(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(RestoreLocators.LOGIN_BUTTON)
        )
        login_button.click()

        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )