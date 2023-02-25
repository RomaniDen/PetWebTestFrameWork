from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum

from pages.base_page import BasePage


class HomePageTitles(Enum):
    uk = 'Автозапчастини EXIST.UA: Запчастини до авто онлайн!'
    en = 'Car Parts Store Exist.ua - Auto Parts Online'
    ru = 'Автозапчасти онлайн: купить запчасти на авто - Exist.ua'


class HomePage(BasePage):
    URL = 'https://exist.ua/'

    def __init__(self, driver):
        super().__init__(driver)
        self.titles = HomePageTitles


    def load_page(self):
        """ Opens current page URL, and returns page load time """
        self.driver.get(self.URL)
        # Wait for the page to load completely (i.e. until the 'body' tag is present)
        wait = WebDriverWait(self.driver, self.DEFAULT_WAIT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # Measure the page load time
        return self.driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart) / 1000;"
        )

    @property
    def is_title_valid(self):
        return self.title == self.titles[self.lang_key].value
