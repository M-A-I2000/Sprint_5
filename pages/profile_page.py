from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.base_locator import BaseLocators
from locators.login_locator import LoginLocators
from locators.profile_locator import ProfileLocators
from curl import *

class ProfilePage(BasePage):

    def open_login_page(self):
        self.click(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    def login(self, username, password):
        self.type(LoginLocators.EMAIL_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def go_to_constructor(self):
        self.click(ProfileLocators.CONSTRUCTOR_BUTTON)

    def click_to_logo(self):
        self.click(BaseLocators.LOGO_BUTTON)

    def find_and_click_logout_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        login_button.click()

        logout_button = self.wait.until(
            EC.element_to_be_clickable((ProfileLocators.LOGOUT_BUTTON))
        )
        logout_button.click()

    def login_button_wait(self):
        self.wait.until(lambda driver: driver.current_url == LOGIN_URL)

        login_button = self.wait.until(
            EC.visibility_of_element_located((LoginLocators.LOGIN_BUTTON))
        )
        return login_button
    
    def personal_account_button_click(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        login_button.click()
    
    def click_to_logo_button(self):
        logo_button = self.wait.until(
            EC.element_to_be_clickable(BaseLocators.LOGO_BUTTON)
        )
        logo_button.click()

    def home_page_wait(self):
        self.wait.until(lambda driver: driver.current_url != BASE_URL + '/account/profile')

    def click_to_constructor_button(self):
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(ProfileLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

    def find_logout_buton(self):
        logout_button = self.wait.until(
            EC.visibility_of_element_located((ProfileLocators.LOGOUT_BUTTON))
        )
        return logout_button
    
    def is_order_button_visible(self):
        return self.is_element_visible(BaseLocators.ORDER_BUTTON)