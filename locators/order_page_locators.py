from selenium.webdriver.common.by import By


class TestLocatorsOrderPage:
    # кнопка Далее
    BUTTON_LATER = [By.XPATH, '//button[contains(text(), "Далее")]']
    # кнопка принятия Куки
    BUTTON_COOKIES = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    # поле Имя
    FIELD_NAME = [By.XPATH, '//input[contains(@placeholder, "Имя")]']
    # поле Фамилия
    FIELD_FAMILY = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]']
    # поле Адрес
    FIELD_ADDRESS = [By.XPATH, '//input[contains(@placeholder, "Адрес")]']
    # поле Метро
    FIELD_METRO = [By.XPATH, '//input[@class = "select-search__input"]']
    # поле Метро - список значений
    FIELD_METRO_LIST = [By.XPATH, '//button[contains(@class, "Order_SelectOption")]']
    # поле Телефон
    FIELD_PHONE = [By.XPATH, '//input[contains(@placeholder, "Телефон")]']
    # логотип Яндекс
    LOGO_YANDEX = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
    # логотип Самокат
    LOGO_SCOOTER = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']
    # поле поиска
    FIELD_SEARCH = [By.XPATH, '//div[contains(@class, "desktop-base-header")]']
    # кнопка Заказать
    BUTTON_ORDER = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[contains(text(), "Заказать")]']
    # поле Когда привезти самокат
    FIELD_DATE = [By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]']
    # поле Срок аренды
    FIELD_PERIOD = [By.XPATH, '//div[contains(@class, "Dropdown-control")]']
    # поле Срок аренды - список значений
    FIELD_PERIOD_LIST = [By.XPATH, '//div[contains(@class, "Dropdown-menu")]']
    # кнопка Заказать
    BUTTON_YES = [By.XPATH, '//button[contains(text(), "Да")]']
    # надпись Заказ оформлен
    LABEL_ORDER_OK = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']
    # Надпись Про аренду
    LABEL_RENT = [By.XPATH, '//div[contains(text(), "Про аренду")]']
