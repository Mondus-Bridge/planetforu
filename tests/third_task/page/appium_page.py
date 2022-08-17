from tests.third_task.page.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


icon_on_the_main_screen = (By.XPATH, '//android.widget.TextView[@content-desc="Planet4Me"]')
login = (By.ID, 'com.planet.forme:id/loginInput')
email = (By.ID, 'com.planet.forme:id/emailInput')
password = (By.ID, 'com.planet.forme:id/passwordInput')
reg_button = (By.ID, 'com.planet.forme:id/registerButton')
popup = (By.ID, 'com.planet.forme:id/closeButton')
search_btn = (By.ID, 'com.planet.forme:id/navigationGlobalSearch')
search_field = (By.ID, 'com.planet.forme:id/searchEditText')
results = (By.ID, 'com.planet.forme:id/searchProfile')


class AppiumPage(BasePage):
    def open_and_autorisation(self, yourlogin, yourmail, yourpassword):
        planet_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(icon_on_the_main_screen))
        planet_icon.click()
        log_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login))
        log_field.click()
        log_field.send_keys(yourlogin)
        email_filed = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(email))
        email_filed.click()
        email_filed.send_keys(yourmail)
        pass_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(password))
        pass_field.click()
        pass_field.send_keys(yourpassword)
        reg_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(reg_button))
        reg_btn.click()


    def search_some_txt(self, text):
        popup_exit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(popup))
        popup_exit.click()
        srch_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_btn))
        srch_btn.click()
        srch_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(search_field))
        srch_field.click()
        srch_field.send_keys(text)

    def should_be_some_result(self):
        result_el = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(results))
        result_list = [el.text for el in result_el]
        return result_list