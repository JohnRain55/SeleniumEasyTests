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
            assert day in self.browser.find_element(*DropDownListLocators.DAY_SELECTED_TEXT).text, \
                f"{day} not in day selected text, but should"
