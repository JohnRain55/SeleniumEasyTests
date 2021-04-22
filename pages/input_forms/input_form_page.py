from ..locators import InputFormLocators
from ..base_page import BasePage
from ..base_page import random_string
from selenium.webdriver.common.keys import Keys


class InputFormPage(BasePage):
    def quest_can_see_first_name_errors(self):
        first_name = self.browser.find_element(*InputFormLocators.FIRST_NAME)
        form_color = self.browser.find_element(*InputFormLocators.COLOR_FIRST_NAME)
        assert form_color.value_of_css_property("border-color") == \
               "rgb(51, 51, 51)", "First name color is not grey, but should"
        first_name.send_keys(random_string(1, 1))
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed under first name, but should not"
        assert self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is not displayed under first name, but should"
        assert form_color.value_of_css_property("border-color") == \
               "rgb(169, 68, 66)", "First name color is not red, but should"
        first_name.send_keys(Keys.BACK_SPACE)
        assert form_color.value_of_css_property("border-color") == \
               "rgb(169, 68, 66)", "First name color is not red, but should"
        assert self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is not displayed under first name, but should"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed under first name, but should not"
        first_name.send_keys(random_string(2, 11))
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed under first name, but should not"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed under first name, but should not"
        assert form_color.value_of_css_property("border-color") == \
               "rgb(60, 118, 61)",  "First name color is not green, but should"

    def quest_can_see_last_name_errors(self):
        last_name = self.browser.find_element(*InputFormLocators.LAST_NAME)
        form_color = self.browser.find_element(*InputFormLocators.COLOR_LAST_NAME)
        assert form_color.value_of_css_property("border-color") == \
               "rgb(51, 51, 51)", "Last name color is not grey, but should"
        last_name.send_keys(random_string(1, 1))
        assert form_color.value_of_css_property("border-color") == \
               "rgb(169, 68, 66)", "Last name color is not red, but should"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed under last name, but should not"
        assert self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is not displayed under last name, but should"
        last_name.send_keys(Keys.BACK_SPACE)
        assert self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is not displayed under last name, but should"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed under last name, but should not"
        assert form_color.value_of_css_property("border-color") == \
               "rgb(169, 68, 66)", "Last name color is not red, but should"
        last_name.send_keys(random_string(2, 11))
        assert not self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed under last name, but should not"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_LAST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed under last name, but should not"
        assert form_color.value_of_css_property("border-color") == \
               "rgb(60, 118, 61)", "Last name color is not green, but should"
