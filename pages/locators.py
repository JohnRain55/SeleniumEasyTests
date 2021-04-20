from selenium.webdriver.common.by import By


class BaseLocators:
    EXIT_ALERT = (By.CSS_SELECTOR, "a#at-cv-lightbox-close")


class SimpleFormPageLocators:
    ENTER_MESSAGE = (By.CSS_SELECTOR, "input#user-message")
    SHOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[onclick=\"showInput();\"]")
    TEXT_MESSAGE = (By.CSS_SELECTOR, "span#display")
    NUM_ONE = (By.CSS_SELECTOR, "input#sum1")
    NUM_TOO = (By.CSS_SELECTOR, "input#sum2")
    SUM_BUTTON = (By.CSS_SELECTOR, "button[onclick=\"return total()\"]")
    SUM = (By.CSS_SELECTOR, "#displayvalue")


class CheckboxPageLocators:
    CLICK_ON_THIS_CHECKBOX = (By.CSS_SELECTOR, "input#isAgeSelected")
    CHECKBOX_TEXT = (By.CSS_SELECTOR, "div#txtAge")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type=\"checkbox\"]")
    CHECK_ALL_BUTTON = (By.CSS_SELECTOR, "#check1")


class RadioButtonPageLocators:
    RADIO_BUTTON_MALE = (By.CSS_SELECTOR, "[name=\"optradio\"][value=\"Male\"]")
    RADIO_BUTTON_FEMALE = (By.CSS_SELECTOR, "[name=\"optradio\"][value=\"Female\"]")
    BUTTON_CHECK_MALE_OR_FEMALE = (By.CSS_SELECTOR, "#buttoncheck")
    CHECKING_TEXT = (By.CSS_SELECTOR, "[class=\"radiobutton\"]")
