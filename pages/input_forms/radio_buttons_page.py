from ..locators import RadioButtonPageLocators
from ..base_page import BasePage
from random import choice


class RadioButtonsPage(BasePage):

    def should_be_elements(self):
        self.should_be_radio_button_male()
        self.should_be_radio_button_female()
        self.should_be_button_check_male_or_female()
        self.should_be_emerging_text()
        self.should_text_be_undisplayed()
        self.should_be_radio_sex_male()
        self.should_be_radio_sex_female()
        self.should_be_radio_age_0_5()
        self.should_be_radio_age_5_15()
        self.should_be_radio_age_15_50()
        self.should_be_button_get_values()
        self.should_be_sex_values()
        self.should_not_be_age_value()
        self.should_be_undisplayed_sex()

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

    def should_be_radio_sex_male(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_SEX_MALE), \
            'Radio sex male is not present, but should'

    def should_be_radio_sex_female(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_SEX_FEMALE), \
            'Radio sex female is not present, but should'

    def should_be_radio_age_0_5(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_AGE_GROUP_0_5), \
            'Radio age group 0 - 5  is not present, but should'

    def should_be_radio_age_5_15(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_AGE_GROUP_5_15), \
            'Radio age group 5 - 15  is not present, but should'

    def should_be_radio_age_15_50(self):
        assert self.is_element_present(*RadioButtonPageLocators.RADIO_AGE_GROUP_15_50), \
            'Radio age group 15 - 50  is not present, but should'

    def should_be_button_get_values(self):
        assert self.is_element_present(*RadioButtonPageLocators.BUTTON_GET_VALUES), \
            "Button get values is not present, but should"

    def should_be_sex_values(self):
        assert self.is_element_present(*RadioButtonPageLocators.SEX_VALUE), \
            "Sex values is not present, but should"

    def should_not_be_age_value(self):
        assert not self.is_element_present(*RadioButtonPageLocators.AGE_VALUE), \
            "Age values is present, but should not"

    def should_be_undisplayed_sex(self):
        assert not self.is_element_displayed(*RadioButtonPageLocators.SEX_VALUE), \
            "Sex values  displayed, but should not"

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

    def quest_two(self):
        rb_male = self.browser.find_element(*RadioButtonPageLocators.RADIO_SEX_MALE)
        rb_female = self.browser.find_element(*RadioButtonPageLocators.RADIO_SEX_FEMALE)
        male_or_female = choice([rb_male, rb_female])
        male_or_female.click()
        rb_0_5 = self.browser.find_element(*RadioButtonPageLocators.RADIO_AGE_GROUP_0_5)
        rb_5_15 = self.browser.find_element(*RadioButtonPageLocators.RADIO_AGE_GROUP_5_15)
        rb_15_50 = self.browser.find_element(*RadioButtonPageLocators.RADIO_AGE_GROUP_15_50)
        age = choice([rb_0_5, rb_5_15, rb_15_50])
        age.click()
        button_value = self.browser.find_element(*RadioButtonPageLocators.BUTTON_GET_VALUES)
        button_value.click()
        assert male_or_female.get_attribute("value") \
               in self.browser.find_element(*RadioButtonPageLocators.SEX_VALUE).text, "Sex shown wrong"
        assert age.get_attribute("value").replace("to", '-') \
               in self.browser.find_element(*RadioButtonPageLocators.SEX_VALUE).text, "Age shown wrong"
