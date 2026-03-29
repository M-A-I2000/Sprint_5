from pages.base_page import BasePage
from locators.base_locator import BaseLocators
from locators.registration_locator import RegistrationLocators
from curl import REGISTER_URL, BASE_URL


class RegistrationPage(BasePage):

    def open_registration_page(self):
        self.open(REGISTER_URL)

    def login(self, name, email, password):
        self.type(RegistrationLocators.NAME_INPUT, name)
        self.type(RegistrationLocators.EMAIL_INPUT, email)
        self.type(RegistrationLocators.PASSWORD_INPUT, password)
        self.click(RegistrationLocators.REGISTRATION_BUTTON)

    def successful_registration(self):
        self.wait.until(lambda driver: driver.current_url != BASE_URL + '/register')