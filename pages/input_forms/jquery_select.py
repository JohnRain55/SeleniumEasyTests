from ..locators import JQuerySelectLocators
from ..base_page import BasePage


class JQuerySelectPage(BasePage):
    def should_be_elements(self):
        self.should_be_select_country()
        self.should_be_select_state()
        self.should_be_select_territories()
        self.should_be_select_file()

    def should_be_select_country(self):
        assert self.is_element_present(*JQuerySelectLocators.SELECT_COUNTRY), \
            "Select country is not present, but should"

    def should_be_select_state(self):
        assert self.is_element_present(*JQuerySelectLocators.SELECT_STATE), "Select state is not present, but should"

    def should_be_select_territories(self):
        assert self.is_element_present(*JQuerySelectLocators.SELECT_TERRITORIES), \
            "Select territories is not present, but should"

    def should_be_select_file(self):
        assert self.is_element_present(*JQuerySelectLocators.SELECT_FILE), "Select file is not present, but should"
