from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент {locator} c ожиданием его видимости и возвращаем его')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу {locator} с ожиданием его кликабельности')
    def click_to_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Передаем элементу {locator} значение "{text}" с ожиданием его видимости')
    def set_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем text от элемента {locator} с ожиданием его видимости')
    def get_text_from_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.find_element_with_wait(locator).text
