from .pages.input_forms.input_form_page import InputFormPage

link = "https://www.seleniumeasy.com/test/input-form-demo.html"


def test_quest_can_see_first_name_errors(browser):
    page = InputFormPage(browser, link)
    page.open()
    page.quest_can_see_first_name_errors()


def test_quest_can_see_last_name_errors(browser):
    page = InputFormPage(browser, link)
    page.open()
    page.quest_can_see_last_name_errors()
