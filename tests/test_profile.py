from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locator import ProfileLocators
from pages.profile_page import ProfilePage
from locators.base_locator import BaseLocators
from curl import *

class TestProfilePage:

    def test_click_personal_account_button_opens_personal_account_page(self, authorized_user): #переход в ЛК
        page = ProfilePage(authorized_user)
        page.personal_account_button_click()
        logout_button = page.find_logout_buton()

        assert logout_button.is_displayed()


    def test_click_constructor_button_opens_constructor_page(self, authorized_user): #переход в Конструктор из ЛК
        page = ProfilePage(authorized_user)
        page.personal_account_button_click()
        page.home_page_wait()
        page.click_to_constructor_button()

        assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)


    def test_logo_click_navigates_to_homepage(self, authorized_user): #переход на главную страницу по клику на лого
        page = ProfilePage(authorized_user)
        page.personal_account_button_click()
        page.home_page_wait()
        page.click_to_logo_button()

        assert EC.visibility_of_element_located(BaseLocators.ORDER_BUTTON)