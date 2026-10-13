from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
