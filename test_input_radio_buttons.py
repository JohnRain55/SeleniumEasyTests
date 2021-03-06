from .pages.input_forms.radio_buttons_page import RadioButtonsPage


link = "https://www.seleniumeasy.com/test/basic-radiobutton-demo.html"


def test_is_elements_present(browser):
    page = RadioButtonsPage(browser, link)
    page.open()
    page.should_be_elements()


def test_quest_one(browser):
    page = RadioButtonsPage(browser, link)
    page.open()
    page.quest_one()


def test_quest_two(browser):
    page = RadioButtonsPage(browser, link)
    page.open()
    page.quest_two()


def test_quest_one_and_two(browser):
    page = RadioButtonsPage(browser, link)
    page.open()
    page.quest_one()
    page.quest_two()
