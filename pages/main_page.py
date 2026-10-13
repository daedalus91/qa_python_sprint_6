import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)

    @allure.step("Нажать кнопку «Заказать» ({position})")
    def click_order_button(self, position):
        locators = {
            "top": MainPageLocators.ORDER_BUTTON_TOP,
            "bottom": MainPageLocators.ORDER_BUTTON_BOTTOM,
        }
        self.click(locators[position])

    @allure.step("Нажать на вопрос №{index}")
    def click_faq_question(self, index):
        self.click(MainPageLocators.faq_question(index))

    @allure.step("Получить текст ответа №{index}")
    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step("Проверить, что открыта главная страница")
    def is_main_page_opened(self):
        return self.is_visible(MainPageLocators.ORDER_BUTTON_TOP)
