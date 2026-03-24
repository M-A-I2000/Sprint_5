from selenium.webdriver.common.by import By

class ConstructorLocators():
    ROLLS_SECTION = (By.XPATH, "//div/main/section[1]/div[1]/div[1]")
    ROLLS_LIST = (By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a")
    SAUCES_SECTION = (By.XPATH, "//div/main/section[1]/div[1]/div[2]")
    SAUCES_LIST = (By.XPATH, "//div/main/section[1]/div[2]/ul[2]/a")
    FILLING_SECTION = (By.XPATH, "//div/main/section[1]/div[1]/div[3]")
    FILLING_LIST = (By.XPATH, "//div/main/section[1]/div[2]/ul[3]/a")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")