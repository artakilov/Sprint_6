import pytest
from locators.order_page_locators import TestLocatorsOrderPage
from pages.order_page import OrderPage
import data_for_tests as dft
from conftest import driver_order
import allure


class TestOrderPage:

    # тесты 011 - 012 - позитивные, проверка оформления заказа
    @allure.title('Проверка оформления заказа {order[6]}')
    @allure.description('На странице заполняем обязательные поля и оформляем заказ. '
                        'Проверяем, что появилось сообщение "Заказ оформлен"')
    @pytest.mark.parametrize('order', dft.orders)
    def test_add_order(self, driver_order, order):
        order_page = OrderPage(driver_order)
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.BUTTON_COOKIES)
        order_page.input_order_form_1(order[0], order[1], order[2], order[3], order[4])
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.BUTTON_LATER)
        order_page.input_order_form_2(order[5])
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.BUTTON_ORDER)
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.BUTTON_YES)
        assert "Заказ оформлен" in order_page.get_text_from_element_with_wait(TestLocatorsOrderPage.LABEL_ORDER_OK), \
            f'Заказ {order[6]} не оформляется!'

    # тест 013 - позитивный, проверка перехода по клику на логотип Яндекс
    @allure.title('Проверка перехода по клику на логотип Яндекс')
    @allure.description('На странице кликаем на логотип Яндекс и проверяем, что в новом окне через редирект '
                        'открывается главная страница Дзена')
    def test_ckick_logo_yandex(self, driver_order):
        order_page = OrderPage(driver_order)
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.LOGO_YANDEX)
        order_page.switch_to_window_and_wait_for_load(TestLocatorsOrderPage.FIELD_SEARCH)
        assert driver_order.current_url == dft.URL_DZEN, \
            f'При клике на лого Яндекс главная страница Дзена не открывается в новом окне через редирект!'

    # тест 014 - позитивный, проверка перехода по клику на логотип Самокат
    @allure.title('Проверка перехода по клику на логотип Самокат')
    @allure.description('На странице кликаем на логотип Самокат и проверяем, что происходит переход на главную '
                        'страницу Самокат')
    def test_ckick_logo_scooter(self, driver_order):
        order_page = OrderPage(driver_order)
        order_page.click_to_element_with_wait(TestLocatorsOrderPage.LOGO_SCOOTER)
        assert driver_order.current_url == dft.URL_SCOOTER, \
            f'При клике на лого Самокат не происходит переход на главную страницу Самоката!'
