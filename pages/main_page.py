from pages.base_page import BasePage
import allure


# Класс главной страницы Самоката
class MainPage(BasePage):

    @allure.step('Получаем текст ответа {locator_a} на вопрос {locator_q}')
    def get_answer_text(self, locator_q, locator_a):
        self.scroll_and_click_to_element(locator_q)
        return self.get_text_from_element_with_wait(locator_a)
