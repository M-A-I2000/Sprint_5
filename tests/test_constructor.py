from pages.constructor_page import ConstructorPage
from curl import *

class TestConstructorPage:

    def test_click_buns_section_navigates_to_rolls(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        page.constructor_button()
        page.click_sauces_section()
        page.click_rolls_section()

        rolls_cards = page.get_rolls_cards()
        actual_count = len(rolls_cards)

        assert actual_count == 2, (
            f"Неверное количество карточек булок: {actual_count}. "
            f"Ожидалось: 2"
        )


    def test_click_sauces_section_navigates_to_sauces(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        page.constructor_button()
        page.click_sauces_section()

        sauces_cards = page.get_sauces_cards()
        actual_count = len(sauces_cards)

        assert actual_count == 4, (
            f"Неверное количество карточек соусов: {actual_count}. "
            f"Ожидалось: 4"
        )


    def test_click_fillings_section_navigates_to_fillings(self, driver):
        page = ConstructorPage(driver)
        page.open_constructor_page()
        page.constructor_button()
        page.click_filling_section()

        fillings_cards = page.get_filling_cards()
        actual_count = len(fillings_cards)

        assert actual_count == 9, (
            f"Неверное количество карточек начинок: {actual_count}. "
            f"Ожидалось: 9"
        )