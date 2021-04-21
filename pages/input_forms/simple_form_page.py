from pages.locators import SimpleFormPageLocators
from pages.base_page import BasePage
from pages.base_page import random_string
from pages.base_page import random_num


class SimpleFormPage(BasePage):
    def should_be_elements(self):
        self.should_be_enter_message_form()
        self.should_be_show_message_button()
        self.should_be_text_message()
        self.should_be_num_one_form()
        self.should_be_num_too_form()
        self.should_be_sum_button()
        self.should_be_sum_text()

    def should_be_enter_message_form(self):
        assert self.is_element_present(*SimpleFormPageLocators.ENTER_MESSAGE), "Enter message form is not present"

    def should_be_show_message_button(self):
        assert self.is_element_present(*SimpleFormPageLocators.SHOW_MESSAGE_BUTTON),\
            "Show message button is not present"

    def should_be_text_message(self):
        assert self.is_element_present(*SimpleFormPageLocators.TEXT_MESSAGE), "Text message is not present"

    def should_be_num_one_form(self):
        assert self.is_element_present(*SimpleFormPageLocators.NUM_ONE), "Num one form is not present"

    def should_be_num_too_form(self):
        assert self.is_element_present(*SimpleFormPageLocators.NUM_TOO), "Num too form is not present"

    def should_be_sum_button(self):
        assert self.is_element_present(*SimpleFormPageLocators.SUM_BUTTON), "Sum button is not present"

    def should_be_sum_text(self):
        assert self.is_element_present(*SimpleFormPageLocators.SUM), "Sum one and too is not present"

    def quest_one(self):
        input_1 = self.browser.find_element(*SimpleFormPageLocators.ENTER_MESSAGE)
        input_text = random_string()
        input_1.send_keys(input_text)
        button = self.browser.find_element(*SimpleFormPageLocators.SHOW_MESSAGE_BUTTON)
        button.click()
        text = self.browser.find_element(*SimpleFormPageLocators.TEXT_MESSAGE).text
        assert input_text == text, "Input text differs from displayed text"

    def quest_two(self):
        num_one = self.browser.find_element(*SimpleFormPageLocators.NUM_ONE)
        one = random_num()
        num_one.send_keys(one)
        num_too = self.browser.find_element(*SimpleFormPageLocators.NUM_TOO)
        too = random_num()
        num_too.send_keys(too)
        button = self.browser.find_element(*SimpleFormPageLocators.SUM_BUTTON)
        button.click()
        sum_one_and_too = self.browser.find_element(*SimpleFormPageLocators.SUM).text
        assert one + too == int(sum_one_and_too), "Inputs sum differs from calculated sum"
