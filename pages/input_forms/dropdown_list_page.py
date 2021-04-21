from pages.locators import DropDownListLocators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class DropDownListPage(BasePage):
    def quest_one(self):
        select_day = Select(self.browser.find_element(*DropDownListLocators.SELECT_DAY))
        for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            select_day.select_by_value(day)
            assert day in self.browser.find_element(*DropDownListLocators.DAY_SELECTED_TEXT).text, \
                f"{day} not in day selected text, but should"
