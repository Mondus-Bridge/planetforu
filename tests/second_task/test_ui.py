from ..page.yandex_page import YandexPage
from ..page.main_planetfor import PlanetforPage


def test_yandex(browser):
    URL = 'https://www.yandex.ru'
    page = YandexPage(browser, URL)
    page.open()
    text = 'Planet for me'
    page.write_text_in_search_field(text)
    assert 'planetfor.me' in page.should_be_planet_in_search_results(), "planetfor.me is not founded"


def test_planetforme(browser):
    URL = 'https://planetfor.me'
    page = PlanetforPage(browser, URL)
    page.open()
    text = 'qa'
    page.write_text_in_search_field(text)
    assert len(page.should_be_some_result()) >= 1, "result not found"
    assert page.should_be_current_url_with_right_query() == f'https://planetfor.me/search?inquiry={text}', "url is diffirent from query"
