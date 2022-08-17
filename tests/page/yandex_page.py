from .base_page import BasePage
from .locators import YandexPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class YandexPage(BasePage):
    def write_text_in_search_field(self, text):
        el = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(YandexPageLocators.SEARCH_FIELD))
        el.click()
        el.send_keys(text)
        el2 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(YandexPageLocators.SEARCH_BUTTON))
        action = ActionChains(self.browser)
        action.move_to_element(el2).click().perform()

    def should_be_planet_in_search_results(self):
        elements = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(YandexPageLocators.LIST_OF_RESULT))
        result = [i.text for i in elements]
        return result



