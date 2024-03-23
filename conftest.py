import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_main():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_order():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    driver.get('https://qa-scooter.praktikum-services.ru/order')
    yield driver
    driver.quit()
