from pages.input_forms.dropdown_list_page import DropDownListPage


link = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"


def test_should_be_elements(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.should_be_elements()


def test_quest_one(browser):
    page = DropDownListPage(browser, link)
    page.open()
    page.quest_one()
