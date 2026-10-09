import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_page_locators import HeaderLocators


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click(self, locator):
        self.scroll_to(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Принять cookies")
    def accept_cookies(self):
        if self.is_visible(HeaderLocators.COOKIE_BUTTON):
            self.click(HeaderLocators.COOKIE_BUTTON)

    @allure.step("Нажать на логотип «Самоката»")
    def click_scooter_logo(self):
        self.click(HeaderLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(HeaderLocators.LOGO_YANDEX)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться, что URL содержит {part}")
    def wait_url_contains(self, part, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(part))
        return self.driver.current_url
