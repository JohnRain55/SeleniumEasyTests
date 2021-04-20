import pytest
from pages.input_forms.checkbox_page import CheckboxPage


link = "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"


def test_quest_one(browser):
    page = CheckboxPage(browser, link)
    page.open()
    page.quest_one()


def test_quest_too(browser):
    page = CheckboxPage(browser, link)
    page.open()
    page.quest_too()


@pytest.mark.xfail(reason="Bug, if checkbox one is selected, button 'Check All' does not work correctly ")
def test_quest_one_and_too(browser):
    page = CheckboxPage(browser, link)
    page.open()
    page.quest_one()
    page.quest_too()


def test_check_check_button(browser):
    page = CheckboxPage(browser, link)
    page.open()
    page.check_check_button()