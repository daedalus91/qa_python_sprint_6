from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    @staticmethod
    def metro_option(station):
        return By.XPATH, f"//div[@class='select-search__select']//div[text()='{station}']"

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # ввод дд.мм.гггг + Enter
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Назад']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    @staticmethod
    def rental_period_option(period):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"

    @staticmethod
    def color_checkbox(color):
        return By.ID, color

    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    CONFIRM_NO_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Нет']")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') "
                                      "and contains(text(), 'Заказ оформлен')]")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
