from pages.locators import DropDownListLocators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from random import choice


class DropDownListPage(BasePage):
    def should_be_elements(self):
        self.should_be_select_day()
        self.should_be_select_day_text()
        self.should_be_undisplayed_select_day_text()
        self.should_be_select_city()
        self.should_be_first_selected_button()
        self.should_be_all_selected_button()
        self.should_be_city_selected_text()
        self.should_be_undisplayed_city_selected_text()

    def should_be_select_day(self):
        assert self.is_element_present(*DropDownListLocators.SELECT_DAY), \
            "Select day is not present, but should"

    def should_be_select_day_text(self):
        assert self.is_element_present(*DropDownListLocators.DAY_SELECTED_TEXT), \
            "Select day text is not present, but should"

    def should_be_undisplayed_select_day_text(self):
        assert not self.is_element_displayed(*DropDownListLocators.DAY_SELECTED_TEXT), \
            "Select day text is  displayed, but should not"

    def should_be_select_city(self):
        assert self.is_element_present(*DropDownListLocators.SELECT_CITY), \
            "Select city is not present, but should"

    def should_be_first_selected_button(self):
        assert self.is_element_present(*DropDownListLocators.FIRST_SELECTED_CITY_BUTTON), \
            "First selected button is not present, but should"

    def should_be_all_selected_button(self):
        assert self.is_element_present(*DropDownListLocators.ALL_SELECTED_CITY_BUTTON), \
            "All selected button is not present, but should"

    def should_be_city_selected_text(self):
        assert self.is_element_present(*DropDownListLocators.CITY_SELECTED_TEXT), \
            "City selected text is not present, but should"

    def should_be_undisplayed_city_selected_text(self):
        assert not self.is_element_displayed(*DropDownListLocators.CITY_SELECTED_TEXT), \
            "City selected text is  displayed, but should not"

    def quest_one(self):
        select_day = Select(self.browser.find_element(*DropDownListLocators.SELECT_DAY))
        for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            select_day.select_by_value(day)
            assert f"Day selected :- {day}" == self.browser.find_element(*DropDownListLocators.DAY_SELECTED_TEXT).text,\
                f"Day selected text  has incorrect text with the value {day}"

    def quest_two_first_select_button(self):
        select_city = Select(self.browser.find_element(*DropDownListLocators.SELECT_CITY))
        get_first_button = self.browser.find_element(*DropDownListLocators.FIRST_SELECTED_CITY_BUTTON)
        city_list = ["California", "Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]
        select_first = choice(city_list)
        select_city.select_by_value(select_first)
        city_list.remove(select_first)
        for i in range(len(city_list)):
            select_one_city = choice(city_list)
            select_city.select_by_value(select_one_city)
            city_list.remove(select_one_city)
            get_first_button.click()
            assert f"First selected option is : {select_first}" == \
                   self.browser.find_element(*DropDownListLocators.CITY_SELECTED_TEXT).text, \
                f"First selected text should have {select_first}, but it dont"
            select_city.select_by_value(select_one_city)

    def quest_two_all_select_button(self):
        select_city = Select(self.browser.find_element(*DropDownListLocators.SELECT_CITY))
        get_all_button = self.browser.find_element(*DropDownListLocators.ALL_SELECTED_CITY_BUTTON)
        city_list = ["California", "Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]
        select_first_city = choice(city_list)
        city_list.remove(select_first_city)
        select_city.select_by_value(select_first_city)
        all_selected_city = f" {select_first_city}"
        for city in city_list:
            get_all_button.click()
            assert f"Options selected are :{all_selected_city}" == \
                   self.browser.find_element(*DropDownListLocators.CITY_SELECTED_TEXT).text, \
                f"All selected text has incorrect text with selected values {all_selected_city}"
            all_selected_city += " " + city
            select_one_city = choice(city_list)
            select_city.select_by_value(select_one_city)
            city_list.remove(select_one_city)
