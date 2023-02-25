import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from config import Config
from pages.home_page import HomePage


@pytest.fixture(scope='session')
def driver_config(request):
    config_name = request.config.getoption('--config')
    if config_name == 'desktop':
        config = Config.desktop
    elif config_name == 'tablet':
        config = Config.tablet
    elif config_name == 'mobile':
        config = Config.mobile
    else:
        raise ValueError('Invalid configuration name')
    return config


@pytest.fixture(scope='session')
def driver(driver_config):
    # browser = driver_config['browser']
    window_size = driver_config['window_size']
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(*window_size)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    # pytest --config=desktop
    # pytest --config=tablet
    # pytest --config=mobile
    parser.addoption('--config', action='store', default='desktop', help='configuration to use')


@pytest.fixture(scope='module')
def home_page(driver):
    return HomePage(driver)
