from pages.base_page import BasePage
from locators.login_locator import LoginLocators
from curl import LOGIN_URL

class LoginPage(BasePage):

    def open_login_page(self):
        self.open(LOGIN_URL)

    def login(self, username, password):
        self.type(LoginLocators.EMAIL_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

