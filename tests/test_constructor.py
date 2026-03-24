from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constructor_page import ConstructorPage
from locators.constructor_locator import ConstructorLocators
from curl import *

def test_click_buns_section_navigates_to_rolls(driver):
    page = ConstructorPage(driver)
    page.open_constructor_page()
    page.constructor_button()

    wait = WebDriverWait(driver, 15) #Необходимо сначала перейти в другой раздел, поскольку по умолчанию мы находися в разделе "Булки"
    element = wait.until(
        EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION),
        message="Элемент вкладки «Булки» не стал кликабельным"
    )
    element.click()

    wait = WebDriverWait(driver, 15)
    element = wait.until(
        EC.element_to_be_clickable(ConstructorLocators.ROLLS_SECTION),
        message="Элемент вкладки «Булки» не стал кликабельным"
    )
    element.click()

    wait = WebDriverWait(driver, 10)
    rolls_cards = wait.until(
        EC.visibility_of_all_elements_located((ConstructorLocators.ROLLS_LIST))
    )

    actual_count = len(rolls_cards)
    assert actual_count == 2, (
        f"Неверное количество карточек соусов: {actual_count}. "
        f"Ожидалось: 2"
    )


def test_click_sauces_section_navigates_to_sauces(driver):
    page = ConstructorPage(driver)
    page.open_constructor_page()
    page.constructor_button()

    wait = WebDriverWait(driver, 15)
    element = wait.until(
        EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION),
        message="Элемент вкладки «Булки» не стал кликабельным"
    )
    element.click()

    wait = WebDriverWait(driver, 10)
    rolls_cards = wait.until(
        EC.visibility_of_all_elements_located((ConstructorLocators.SAUCES_LIST))
    )

    actual_count = len(rolls_cards)
    assert actual_count == 4, (
        f"Неверное количество карточек соусов: {actual_count}. "
        f"Ожидалось: 4"
    )

    #assert len(rolls_cards) > 0, "Раздел «Соусы» не загрузился — карточки не найдены"



def test_click_fillings_section_navigates_to_fillings(driver):
    page = ConstructorPage(driver)
    page.open_constructor_page()
    page.constructor_button()

    wait = WebDriverWait(driver, 15)
    element = wait.until(
        EC.element_to_be_clickable(ConstructorLocators.FILLING_SECTION),
        message="Элемент вкладки «Булки» не стал кликабельным"
    )
    element.click()

    wait = WebDriverWait(driver, 10)
    rolls_cards = wait.until(
        EC.visibility_of_all_elements_located((ConstructorLocators.FILLING_LIST))
    )

    actual_count = len(rolls_cards)
    assert actual_count == 9, (
        f"Неверное количество карточек соусов: {actual_count}. "
        f"Ожидалось: 9"
    )