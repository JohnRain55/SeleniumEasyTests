from pages.locators import RadioButtonPageLocators
from pages.base_page import BasePage


class RadioButtonsPage(BasePage):

    def should_be_elements(self):
        self.should_be_radio_button_male()
        self.should_be_radio_button_female()
        self.should_be_button_check_male_or_female()
        self.should_be_emerging_text()
        self.should_text_be_undisplayed()

    def should_be_radio_button_male(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_BUTTON_MALE), \
            "Radio button male is not present, but should"

    def should_be_radio_button_female(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_BUTTON_FEMALE), \
            "Radio button female is not present, but should"

    def should_be_button_check_male_or_female(self):
        assert self.is_element_present(*RadioButtonPageLocators.BUTTON_CHECK_MALE_OR_FEMALE), \
            "Button for check  male or female is not present, but should"

    def should_be_emerging_text(self):
        assert self.is_element_present(*RadioButtonPageLocators.CHECKING_TEXT), \
            "Emerging text is not present, but should"

    def should_text_be_undisplayed(self):
        assert not self.is_element_displayed(*RadioButtonPageLocators.CHECKING_TEXT), \
            "Checking text is displayed, but should not"

    def quest_one(self):
        button_check = self.browser.find_element(*RadioButtonPageLocators.BUTTON_CHECK_MALE_OR_FEMALE)
        button_check.click()
        assert "Radio button is Not checked" == \
               self.browser.find_element(*RadioButtonPageLocators.CHECKING_TEXT).text, "Verification text wrong"
        rb_male = self.browser.find_element(*RadioButtonPageLocators.RADIO_BUTTON_MALE)
        rb_male.click()
        button_check.click()
        assert "Radio button 'Male' is checked" == \
               self.browser.find_element(*RadioButtonPageLocators.CHECKING_TEXT).text, "Verification text wrong"
        rb_female = self.browser.find_element(*RadioButtonPageLocators.RADIO_BUTTON_FEMALE)
        rb_female.click()
        button_check.click()
        assert "Radio button 'Female' is checked" == \
               self.browser.find_element(*RadioButtonPageLocators.CHECKING_TEXT).text, "Verification text wrong"

