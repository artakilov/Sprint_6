from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure


# Класс страницы заказа
class OrderPage(BasePage):

    @allure.step('Заполняем данными первую форму заказа')
    def input_order_form_1(self, locator_n, locator_f, locator_a, locator_m, locator_ml, locator_p,
                           name, family, address, metro, phone):
        self.set_text_to_field(locator_n, name)
        self.set_text_to_field(locator_f, family)
        self.set_text_to_field(locator_a, address)
        self.set_text_to_field(locator_m, metro)
        self.click_to_element_with_wait(locator_ml)
        self.set_text_to_field(locator_p, phone)

    @allure.step('Заполняем данными вторую форму заказа')
    def input_order_form_2(self, locator_d, locator_p, locator_pl, locator_l, date):
        self.set_text_to_field(locator_d, date)
        self.click_to_element_with_wait(locator_l)
        self.click_to_element_with_wait(locator_p)
        self.click_to_element_with_wait(locator_pl)

    @allure.step('Переключаемся на новую вкладку браузера')
    def switch_to_dzen_window_and_wait_for_load_field_search(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
