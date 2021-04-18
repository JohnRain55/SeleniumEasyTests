from selenium.webdriver.common.by import By


class BaseLocators:
    EXIT_ALERT = (By.CSS_SELECTOR, "a#at-cv-lightbox-close")


class SimpleFormPageLocators:
    ENTER_MESSAGE = (By.CSS_SELECTOR, "input#user-message")
    SHOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[onclick=\"showInput();\"]")
    TEXT_MESSAGE = (By.CSS_SELECTOR, "span#display")
