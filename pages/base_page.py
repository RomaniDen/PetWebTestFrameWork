from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum

from pages.helpers.helpers import wait_condition


class LanguageKeys(Enum):
    ua = 'ua'
    en = 'en'
    ru = 'ru'


class BasePage:
    DEFAULT_WAIT = 10

    def __init__(self, driver):
        self.driver = driver
        self.footer = Footer(driver)
        self.header = Header(driver)

    # Meta field
    @property
    def title(self):
        return self.driver.title

    # Localization field
    @property
    def lang_key(self):
        current_lang_key = self.driver.current_url.split('/')[3]
        if current_lang_key not in ['uk', 'en']:
            return 'ru'
        return current_lang_key

    def _set_lang(self, lang_code):
        lang_button = WebDriverWait(self.driver, self.DEFAULT_WAIT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-label="{lang_code}"]')))
        lang_status = lang_button.get_attribute('data-active')
        if lang_status != 'true':
            lang_button.click()
            wait_condition(WebDriverWait(self.driver, self.DEFAULT_WAIT).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, f'[aria-label="{lang_code}"]'))).get_attribute('data-active') == 'true')

    def set_lang_en(self):
        self._set_lang(LanguageKeys.en.value)

    def set_lang_ua(self):
        self._set_lang(LanguageKeys.ua.value)

    def set_lang_ru(self):
        self._set_lang(LanguageKeys.ru.value)


class Header:
    def __init__(self, driver):
        self.driver = driver
        self.header_container_selector = 'header[data-testid="headerContainer"'

    @property
    def logo(self):
        logo_container = self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="logo"]')
        return logo_container.find_element(By.CSS_SELECTOR, 'svg')

    @property
    def header_container(self):
        header_container = self.driver.find_element(By.CSS_SELECTOR, self.header_container_selector)
        return header_container


class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.footer_container_selector = 'div[class="Footerstyle__FooterContainer-sc-sqw8j4-1 cnZNDh"]'

    @property
    def footer_container(self):
        footer_container = self.driver.find_element(By.CSS_SELECTOR, self.footer_container_selector)
        return footer_container
