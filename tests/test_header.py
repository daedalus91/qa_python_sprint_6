import allure

from data import Urls
from pages.main_page import MainPage


@allure.feature("Шапка сайта")
class TestHeaderLogos:
    @allure.title("Клик по логотипу «Самоката» ведёт на главную страницу")
    def test_scooter_logo_opens_main_page(self, driver, order_page):
        order_page.click_scooter_logo()
        main_page = MainPage(driver)
        assert main_page.get_current_url() == Urls.MAIN_PAGE and main_page.is_main_page_opened()

    @allure.title("Клик по логотипу Яндекса открывает главную Дзена в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, main_page):
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert Urls.DZEN_DOMAIN in main_page.wait_url_contains(Urls.DZEN_DOMAIN)
