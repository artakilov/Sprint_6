from selenium.webdriver.common.by import By


class TestLocatorsMainPage:
    # кнопки вопросов
    BUTTONS_QUESTIONS = [[By.ID, 'accordion__heading-0'],
                         [By.ID, 'accordion__heading-1'],
                         [By.ID, 'accordion__heading-2'],
                         [By.ID, 'accordion__heading-3'],
                         [By.ID, 'accordion__heading-4'],
                         [By.ID, 'accordion__heading-5'],
                         [By.ID, 'accordion__heading-6'],
                         [By.ID, 'accordion__heading-7']]
    # ответы на вопросы
    LABELS_ANSWERS = [[By.ID, 'accordion__panel-0'],
                      [By.ID, 'accordion__panel-1'],
                      [By.ID, 'accordion__panel-2'],
                      [By.ID, 'accordion__panel-3'],
                      [By.ID, 'accordion__panel-4'],
                      [By.ID, 'accordion__panel-5'],
                      [By.ID, 'accordion__panel-6'],
                      [By.ID, 'accordion__panel-7']]
    # кнопка Заказать в верхней части главной страницы
    BUTTON_ORDER_MAIN_UP = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(@class, "Button_Button")]']
    # кнопка Заказать в нижней части главной страницы
    BUTTON_ORDER_MAIN_DOWN = [By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[contains(@class,'
                                        ' "Button_Button")]']
