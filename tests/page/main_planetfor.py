from .base_page import BasePage
from .locators import PlanetMainLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class PlanetforPage(BasePage):
    def write_text_in_search_field(self, text):
        el = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(PlanetMainLocators.SEARCH_FIELD))
        action = ActionChains(self.browser)
        action.move_to_element(el).click().perform()
        el.send_keys(text)
        el.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(PlanetMainLocators.LIST_OF_RESULT))

    def should_be_some_result(self):
        el = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(PlanetMainLocators.LIST_OF_RESULT))
        list_el = [i.text for i in el]
        return list_el

    def should_be_current_url_with_right_query(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(PlanetMainLocators.LIST_OF_RESULT))
        get_url = self.browser.current_url
        return get_url

