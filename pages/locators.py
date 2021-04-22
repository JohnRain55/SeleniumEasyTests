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
    RADIO_SEX_MALE = (By.CSS_SELECTOR, "[name=\"gender\"][value=\"Male\"]")
    RADIO_SEX_FEMALE = (By.CSS_SELECTOR, "[name=\"gender\"][value=\"Female\"]")
    RADIO_AGE_GROUP_0_5 = (By.CSS_SELECTOR, "[name=\"ageGroup\"][value=\"0 - 5\"]")
    RADIO_AGE_GROUP_5_15 = (By.CSS_SELECTOR, "[name=\"ageGroup\"][value=\"5 - 15\"]")
    RADIO_AGE_GROUP_15_50 = (By.CSS_SELECTOR, "[name=\"ageGroup\"][value=\"15 - 50\"]")
    BUTTON_GET_VALUES = (By.CSS_SELECTOR, "[onclick=\"getValues();\"]")
    SEX_VALUE = (By.CSS_SELECTOR, "[class=\"groupradiobutton\"]")
    AGE_VALUE = (By.CSS_SELECTOR, "[class=\"groupradiobutton\"] br")


class DropDownListLocators:
    SELECT_DAY = (By.CSS_SELECTOR, "select#select-demo")
    DAY_SELECTED_TEXT = (By.CSS_SELECTOR, "[class=\"selected-value\"]")
    SELECT_CITY = (By.CSS_SELECTOR, "select#multi-select")
    FIRST_SELECTED_CITY_BUTTON = (By.CSS_SELECTOR, "button#printMe")
    ALL_SELECTED_CITY_BUTTON = (By.CSS_SELECTOR, "button#printAll")
    CITY_SELECTED_TEXT = (By.CSS_SELECTOR, "[class=\"getall-selected\"]")


class InputFormLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[name=\"first_name\"]")
    TEXT_FIRST_NAME_EMPTY = (By.CSS_SELECTOR, "small[data-bv-for=\"first_name\"][data-bv-validator=\"notEmpty\"]")
    TEXT_FIRST_NAME_LENGTH = (By.CSS_SELECTOR, "small[data-bv-for=\"first_name\"][data-bv-validator=\"stringLength\"]")

    LAST_NAME = (By.CSS_SELECTOR, "input[name=\"last_name\"]")
    EMAIL = (By.CSS_SELECTOR, "input[name=\"email\"]")
    PHONE = (By.CSS_SELECTOR, "input[name=\"phone\"]")
    ADDRESS = (By.CSS_SELECTOR, "input[name=\"address\"]")
    CITY = (By.CSS_SELECTOR, "input[name=\"city\"]")
    STATE = (By.CSS_SELECTOR, "select[name=\"state\"]")
    ZIP_CODE = (By.CSS_SELECTOR, "input[name=\"zip\"]")
    WEBSITE = (By.CSS_SELECTOR, "input[name=\"website\"]")
    HOSTING_YES = (By.CSS_SELECTOR, "input[name=\"hosting\"][value=\"yes\"]")
    HOSTING_NO = (By.CSS_SELECTOR, "input[name=\"hosting\"][value=\"no\"]")
    PROJECT_DESCRIPTION = (By.CSS_SELECTOR, "textarea[name=\"comment\"]")
    SEND_BUTTON = (By.CSS_SELECTOR, "button[class=\"btn btn-default\"]")
