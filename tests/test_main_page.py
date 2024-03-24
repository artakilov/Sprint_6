import pytest
from pages.main_page import MainPage
import data_for_tests as dft
from locators.main_page_locators import TestLocatorsMainPage
from conftest import driver_main
import allure


class TestMainPage:

    # тесты 001 - 008 - позитивные, проверка правильности ответов в перечне вопросов
    @allure.title('Проверка правильности ответа на вопрос {(num+1)}')
    @allure.description('На странице кликаем на вопрос {(num+1)} и проверяем, что ответ соответствует ожидаемому')
    @pytest.mark.parametrize('num, answer', dft.answers)
    def test_correct_answers_to_questions(self, driver_main, num, answer):
        main_page = MainPage(driver_main)
        assert main_page.get_answer_text(TestLocatorsMainPage.BUTTONS_QUESTIONS[num],
                                         TestLocatorsMainPage.LABELS_ANSWERS[num]) == answer, \
            (f'Не верный ответ на вопрос "'
             f'{main_page.get_text_from_element_with_wait(TestLocatorsMainPage.BUTTONS_QUESTIONS[num])}"!')

    # тест 009 - позитивный, проверка точки вход в сценарий Заказа через кнопку Заказать в верхней части главной
    # страницы
    @allure.title('Проверка точки вход в сценарий Заказа через кнопку Заказать в верхней части главной страницы')
    @allure.description('На странице кликаем на Заказать и проверяем, что открылась форма оформления заказа')
    def test_order_with_button_order_main_up(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.click_to_element_with_wait(TestLocatorsMainPage.BUTTON_ORDER_MAIN_UP)
        assert driver_main.current_url == dft.URL_SCOOTER + dft.EP_ORDER, \
            f'Не работает кнопка "Заказать" в верхней части главной страницы!'

    # тест 010 - позитивный, проверка точки вход в сценарий Заказа через кнопку Заказать в нижней части главной страницы
    @allure.title('Проверка точки вход в сценарий Заказа через кнопку Заказать в нижней части главной страницы')
    @allure.description('На странице кликаем на Заказать и проверяем, что открылась форма оформления заказа')
    def test_order_with_button_order_main_down(self, driver_main):
        main_page = MainPage(driver_main)
        main_page.scroll_and_click_to_element(TestLocatorsMainPage.BUTTON_ORDER_MAIN_DOWN)
        assert driver_main.current_url == dft.URL_SCOOTER + dft.EP_ORDER, \
            f'Не работает кнопка "Заказать" в нижней части главной страницы!'
