import allure
from selenium.webdriver.common.keys import Keys

from data import Urls
from helpers import generate_delivery_date
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Открыть страницу заказа")
    def open_order_page(self):
        self.open(Urls.ORDER_PAGE)

    @allure.step("Выбрать станцию метро «{station}»")
    def select_metro(self, station):
        self.click(OrderPageLocators.METRO_INPUT)
        self.find_visible(OrderPageLocators.METRO_INPUT).send_keys(station)
        self.click(OrderPageLocators.metro_option(station))

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_customer_form(self, data):
        self.type_text(OrderPageLocators.NAME_INPUT, data["name"])
        self.type_text(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.type_text(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.select_metro(data["metro"])
        self.type_text(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Указать дату доставки {delivery_date}")
    def set_delivery_date(self, delivery_date):
        field = self.find_visible(OrderPageLocators.DATE_INPUT)
        field.send_keys(delivery_date, Keys.ENTER)

    @allure.step("Выбрать срок аренды «{period}»")
    def select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rental_period_option(period))

    @allure.step("Выбрать цвета самоката: {colors}")
    def select_colors(self, colors):
        for color in colors:
            self.click(OrderPageLocators.color_checkbox(color))

    @allure.step("Заполнить форму «Про аренду»")
    def fill_rent_form(self, data):
        self.set_delivery_date(generate_delivery_date(data["days_until_delivery"]))
        self.select_rental_period(data["rental_period"])
        self.select_colors(data["colors"])
        if data["comment"]:
            self.type_text(OrderPageLocators.COMMENT_INPUT, data["comment"])

    @allure.step("Нажать «Заказать» и подтвердить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Оформить заказ")
    def make_order(self, data):
        self.fill_customer_form(data)
        self.fill_rent_form(data)
        self.submit_order()

    @allure.step("Проверить, что появилось окно «Заказ оформлен»")
    def is_success_modal_displayed(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL_HEADER)