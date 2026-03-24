from pages.base_page import BasePage
from locators.base_locator import BaseLocators
from locators.login_locator import LoginLocators
from locators.profile_locator import ProfileLocators

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