import pytest
import data_for_tests as dft
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_main():
    driver = webdriver.Firefox()
    driver.set_window_size(dft.WIDTH, dft.HEIGHT)
    driver.get(dft.URL_SCOOTER)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_order():
    driver = webdriver.Firefox()
    driver.set_window_size(dft.WIDTH, dft.HEIGHT)
    driver.get(dft.URL_SCOOTER + dft.EP_ORDER)
    yield driver
    driver.quit()
