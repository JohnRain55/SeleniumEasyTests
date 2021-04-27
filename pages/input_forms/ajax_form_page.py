from ..locators import AjaxFormLocators
from ..base_page import BasePage


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
    #
    # def should_submit_only_with_name(self):
    #     name = self.browser.find_element(*AjaxFormLocators.NAME)
    #     comment = self.browser.find_element(*AjaxFormLocators.COMMENT)
    #     button = self.browser.find_element(*AjaxFormLocators.SUBMIT)
    #     submit_text = self.browser.find_element(*AjaxFormLocators.TEXT_SUCCESSFULLY)
    #     print("button text1:", button.text)
    #     button.click()
    #     print("button text2:", button.text)
    #     name.send_keys("Suka")
    #     button.click()
    #     print("submit_text1:", submit_text.text)
    #     print("submit_text2:", submit_text.text)
