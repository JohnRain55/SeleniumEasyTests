from pages.locators import DropDownListLocators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class DropDownListPage(BasePage):
    def should_be_elements(self):
        self.should_be_select_day()
        self.should_be_select_day_text()
        self.should_be_undisplayed_select_day_text()

    def should_be_select_day(self):
        assert self.is_element_present(*DropDownListLocators.SELECT_DAY), \
            "Select day is not present, but should"

    def should_be_select_day_text(self):
        assert self.is_element_present(*DropDownListLocators.DAY_SELECTED_TEXT), \
            "Select day text is not present, but should"

    def should_be_undisplayed_select_day_text(self):
        assert not self.is_element_displayed(*DropDownListLocators.DAY_SELECTED_TEXT), \
            "Select day text is  displayed, but should not"

    def quest_one(self):
        select_day = Select(self.browser.find_element(*DropDownListLocators.SELECT_DAY))
        for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            select_day.select_by_value(day)
            assert f"Day selected :- {day}" == self.browser.find_element(*DropDownListLocators.DAY_SELECTED_TEXT).text,\
                f"Day selected text  has incorrect text with the value {day}"

    def quest_two(self):
        select_city = Select(self.browser.find_element(*DropDownListLocators.SELECT_CITY))
        get_first_button = self.browser.find_element(*DropDownListLocators.FIRST_SELECTED_CITY_BUTTON)
        get_all_button = self.browser.find_element(*DropDownListLocators.ALL_SELECTED_CITY_BUTTON)
        all_selected_city = ""
        for city in ["California", "Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]:
            select_city.select_by_value(city)
            get_first_button.click()
            assert f"First selected option is : {city}" == \
                   self.browser.find_element(*DropDownListLocators.CITY_SELECTED_TEXT).text, \
                f"First selected text has incorrect text with value {city}"
            all_selected_city += " " + city
            get_all_button.click()
            assert f"Options selected are :{all_selected_city}" == \
                   self.browser.find_element(*DropDownListLocators.CITY_SELECTED_TEXT).text, \
                f"All selected text has incorrect text with selected values {all_selected_city}"
