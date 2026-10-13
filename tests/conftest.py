import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_main_page()
    page.accept_cookies()
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.open_order_page()
    page.accept_cookies()
    return page
