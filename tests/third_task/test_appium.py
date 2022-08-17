from .page.appium_page import AppiumPage
from .constants import EMAIL, PASSWORD, LOGIN


def test_appium(driver):
    el = AppiumPage(driver)
    el.open_and_autorisation(LOGIN, EMAIL, PASSWORD)
    text = 'Москва'
    el.search_some_txt(text)
    assert len(el.should_be_some_result()) >= 1, 'zero results was founded'

