from pages.base_page import BasePage
from locators.constructor_locator import ConstructorLocators
from curl import *

class ConstructorPage(BasePage):

    def open_constructor_page(self):
        self.open(CONSTRUCTOR_URL)

    def rolls_section(self):
        self.click(ConstructorLocators.ROLLS_SECTION)

    def sauces_section(self):
        self.click(ConstructorLocators.SAUCES_SECTION)

    def filling_section(self):
        self.click(ConstructorLocators.FILLING_SECTION)

    def constructor_button(self):
        self.click(ConstructorLocators.CONSTRUCTOR_BUTTON)