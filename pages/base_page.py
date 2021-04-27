from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from .locators import BaseLocators
from random import choice, randint
from string import ascii_letters


def random_string(start=1, stop=100):
    return ''.join(choice(ascii_letters) for i in range(randint(start, stop)))


def random_num(start=1, stop=1000):
    return randint(start, stop)


def random_number(num):
    return randint(10 ** (num - 1), 10 ** num - 1)


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what,):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_displayed(self, how, what):
        if self.is_element_present(how, what):
            if self.browser.find_element(how, what).is_displayed():
                return True
        return False

    def is_element_have_text(self, how, what, text, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)
        if self.is_element_present(*BaseLocators.EXIT_ALERT):
            self.browser.find_element(*BaseLocators.EXIT_ALERT).click()
