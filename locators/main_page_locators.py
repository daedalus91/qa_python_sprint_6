from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки «Заказать»
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"
