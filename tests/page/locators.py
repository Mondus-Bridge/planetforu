from selenium.webdriver.common.by import By


class YandexPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input.input__control')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button > span.button__text')
    LIST_OF_RESULT = (By.CSS_SELECTOR, 'li.serp-item.serp-item_card > div > div > div> a > b')

class PlanetMainLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input.ml-8')
    LIST_OF_RESULT = (By.CSS_SELECTOR, 'div.items-container > div > a >  div > div.profile__info > div > p')