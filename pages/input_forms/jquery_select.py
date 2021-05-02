from ..locators import JQuerySelectLocators
from ..base_page import BasePage
from selenium.webdriver.support.select import Select
import time

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

    def select_country_correct(self):
        assert not self.is_element_present(*JQuerySelectLocators.COUNTRY_LIST), \
            "Select Country span present, but should not"
        select = self.browser.find_element(*JQuerySelectLocators.SELECT_COUNTRY)
        select.click()
        assert self.is_element_present(*JQuerySelectLocators.COUNTRY_LIST), \
            "Select Country span not present, but should "
        country_list = self.browser.find_elements(*JQuerySelectLocators.COUNTRY_NAMES)
        for country in country_list:
            print(country.text)
            select.click()

        select1 = Select(self.browser.find_element(*JQuerySelectLocators.sk))
        select1.select_by_index(2)

        time.sleep(5)
