from pages.input_forms.dropdown_list_page import DropDownListPage
import pytest


link = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"


def test_should_be_elements(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.should_be_elements()


def test_quest_one(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_one()


@pytest.mark.xfail(reason="Bug, button 'Get First Selected' show last selected item")
def test_quest_two_first_select_button(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_two_first_select_button()


@pytest.mark.xfail(reason="Bug, button 'Get All Selected' show last selected item")
def test_quest_two_all_select_button(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_two_all_select_button()


@pytest.mark.xfail(reason="Bug, fix bugs with quest two")
def test_quest_one_and_two(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_one()
    page.quest_two_first_select_button()
    page.quest_two_all_select_button()
