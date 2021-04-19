from pages.locators import CheckboxPageLocators
from pages.base_page import BasePage
from pages.base_page import random_num


class CheckboxPage(BasePage):
    def should_be_elements(self):
        pass

    def should_be_checkboxes(self):
        pass

    def quest_one(self):
        checkbox_one = self.browser.find_element(*CheckboxPageLocators.CLICK_ON_THIS_CHECKBOX)
        assert not self.is_element_displayed(*CheckboxPageLocators.CHECKBOX_TEXT), "Text is displayed, but should not"
        checkbox_one.click()
        assert self.is_element_displayed(*CheckboxPageLocators.CHECKBOX_TEXT), "Text is not displayed, but should"

    def quest_too(self):
        checkboxes = self.browser.find_elements(*CheckboxPageLocators.CHECKBOXES)
        for checkbox in checkboxes[1:]:
            assert "Check All" in \
                   self.browser.find_element(*CheckboxPageLocators.CHECK_ALL_BUTTON).get_attribute('value'), \
                "Button status is not 'Check All', but should"
            checkbox.click()
        assert "Check All" not in \
               self.browser.find_element(*CheckboxPageLocators.CHECK_ALL_BUTTON).get_attribute('value'), \
            "Button status 'Check All', but should not"

    def check_check_button(self):
        button = self.browser.find_element(*CheckboxPageLocators.CHECK_ALL_BUTTON)
        checkboxes = self.browser.find_elements(*CheckboxPageLocators.CHECKBOXES)
        for checkbox in checkboxes[1:]:
            assert not checkbox.is_selected(), "Checkbox selected, but should not"
        for event in range(random_num(1, 10)):
            checkboxes[random_num(1, 4)].click()
        button.click()
        for checkbox in checkboxes[1:]:
            assert checkbox.is_selected(), "Checkbox not selected, but should"
