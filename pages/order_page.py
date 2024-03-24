from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_page_locators import TestLocatorsOrderPage
import allure


# Класс страницы заказа
class OrderPage(BasePage):

    @allure.step('Заполняем данными первую форму заказа')
    def input_order_form_1(self, name, family, address, metro, phone):
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_NAME, name)
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_FAMILY, family)
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_ADDRESS, address)
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_METRO, metro)
        self.click_to_element_with_wait(TestLocatorsOrderPage.FIELD_METRO_LIST)
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_PHONE, phone)

    @allure.step('Заполняем данными вторую форму заказа')
    def input_order_form_2(self, date):
        self.set_text_to_field(TestLocatorsOrderPage.FIELD_DATE, date)
        self.click_to_element_with_wait(TestLocatorsOrderPage.LABEL_RENT)
        self.click_to_element_with_wait(TestLocatorsOrderPage.FIELD_PERIOD)
        self.click_to_element_with_wait(TestLocatorsOrderPage.FIELD_PERIOD_LIST)
