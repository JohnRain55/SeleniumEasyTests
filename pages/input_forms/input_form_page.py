from ..locators import InputFormLocators
from ..base_page import BasePage
from ..base_page import random_string
from selenium.webdriver.common.keys import Keys


class InputFormPage(BasePage):
    def quest_can_see_first_name_errors(self):
        first_name = self.browser.find_element(*InputFormLocators.FIRST_NAME)
        first_name.send_keys(random_string(1, 1))
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed, but should not"
        assert self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is not displayed, but should"
        first_name.send_keys(Keys.BACK_SPACE)
        assert self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is not displayed, but should"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed, but should not"
        first_name.send_keys(random_string(2, 11))
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_EMPTY), \
            "Text: 'Please supply your first name' is displayed, but should not"
        assert not self.is_element_displayed(*InputFormLocators.TEXT_FIRST_NAME_LENGTH), \
            "Text: 'Please enter more than 2 characters' is displayed, but should not"
