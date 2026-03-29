from selenium.webdriver.common.by import By

class ConstructorLocators():
    ROLLS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    ROLLS_LIST = (By.XPATH, "//a/p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and contains(text(), 'булка')]")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    SAUCES_LIST = (By.XPATH, "//a/p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and contains(text(), 'Соус')]")
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    FILLING_LIST = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul/a")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")