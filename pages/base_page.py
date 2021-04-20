from selenium.common.exceptions import NoSuchElementException
from pages.locators import BaseLocators
from random import choice, randint
from string import ascii_letters


def random_string(start=1, stop=100):
    return ''.join(choice(ascii_letters) for i in range(randint(start, stop)))


def random_num(start=1, stop=1000):
    return randint(start, stop)


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

    def is_element_displayed(self, how, what,):
        if self.is_element_present(how, what):
            if self.browser.find_element(how, what).is_displayed():
                return True
        return False

    def open(self):
        self.browser.get(self.url)
        if self.is_element_present(*BaseLocators.EXIT_ALERT):
            self.browser.find_element(*BaseLocators.EXIT_ALERT).click()
