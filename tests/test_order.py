import allure
import pytest

from data import ORDER_DATA_1, ORDER_DATA_2
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный сценарий заказа: точка входа — кнопка «Заказать» ({entry_point})")
    @pytest.mark.parametrize(
        "entry_point, order_data",
        [
            pytest.param("top", ORDER_DATA_1, id="top_button_data_set_1"),
            pytest.param("bottom", ORDER_DATA_2, id="bottom_button_data_set_2"),
        ],
    )
    def test_order_scooter_success(self, driver, main_page, entry_point, order_data):
        main_page.click_order_button(entry_point)
        order_page = OrderPage(driver)
        order_page.make_order(order_data)
        assert order_page.is_success_modal_displayed()
