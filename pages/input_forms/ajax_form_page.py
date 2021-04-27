from ..locators import AjaxFormLocators
from ..base_page import BasePage
from ..base_page import random_string


class AjaxFormPage(BasePage):
    def should_be_elements(self):
        self.should_be_name_area()
        self.should_be_text_area()
        self.should_be_button()

    def should_be_name_area(self):
        assert self.is_element_present(*AjaxFormLocators.NAME), "Name area is not present, bu should"

    def should_be_text_area(self):
        assert self.is_element_present(*AjaxFormLocators.COMMENT), "Text area is not present, bu should"

    def should_be_button(self):
        assert self.is_element_present(*AjaxFormLocators.SUBMIT), "Submit button is not present, bu should"

    def should_submit_only_with_name(self):
        comment = self.browser.find_element(*AjaxFormLocators.COMMENT)
        comment.send_keys(random_string())
        button = self.browser.find_element(*AjaxFormLocators.SUBMIT)
        button.click()
        assert self.is_element_present(*AjaxFormLocators.SUBMIT), "Bottom is not present, but should"
        name = self.browser.find_element(*AjaxFormLocators.NAME)
        name.send_keys(random_string())
        button.click()
        assert self.is_element_have_text(*AjaxFormLocators.TEXT_SUCCESSFULLY, "Form submited Successfully!"), \
            "Text 'Form submited Successfully!' is not displayed, but should"
