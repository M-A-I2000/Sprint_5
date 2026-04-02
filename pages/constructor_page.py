from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.constructor_locator import ConstructorLocators
from curl import *

class ConstructorPage(BasePage):

    def open_constructor_page(self):
        self.open(CONSTRUCTOR_URL)
    
    def click_rolls_section(self):
        element = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.ROLLS_SECTION),
            message="Элемент вкладки «Булки» не стал кликабельным"
        )
        element.click()

    def get_rolls_cards(self):
        cards = self.wait.until(
            EC.visibility_of_all_elements_located((ConstructorLocators.ROLLS_LIST))
        )
        visible_sauces = [card for card in cards if card.is_displayed()]
        return visible_sauces

    def click_sauces_section(self):
        element = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION),
            message="Элемент вкладки «Соусы» не стал кликабельным"
        )
        element.click()

    def get_sauces_cards(self):
        cards = self.wait.until(
            EC.visibility_of_all_elements_located((ConstructorLocators.SAUCES_LIST))
        )
        visible_sauces = [card for card in cards if card.is_displayed()]
        return visible_sauces
    
    def click_filling_section(self):
        element = self.wait.until(
            EC.element_to_be_clickable(ConstructorLocators.FILLING_SECTION),
            message="Элемент вкладки «Начинки» не стал кликабельным"
        )
        element.click()

    def get_filling_cards(self):
        cards = self.wait.until(
            EC.visibility_of_all_elements_located((ConstructorLocators.FILLING_LIST))
        )
        visible_fillings = [card for card in cards if card.is_displayed()]
        return visible_fillings       

    def constructor_button(self):
        self.click(ConstructorLocators.CONSTRUCTOR_BUTTON)
    