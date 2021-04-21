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


@pytest.mark.xfail(reason="Bug, button 'Get All Selected' shou only first selected item")
def test_quest_two(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_two()


@pytest.mark.xfail(reason="Bug, button 'Get All Selected' shou only first selected item")
def test_quest_one_and_two(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_one()
    page.quest_two()
