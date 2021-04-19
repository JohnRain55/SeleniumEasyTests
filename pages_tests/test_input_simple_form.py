from pages.input_forms.simple_form import SimpleFormPage


link = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"


def test_should_be_elements(browser):
    page = SimpleFormPage(browser, link)
    page.open()
    page.should_be_elements()


def test_quest_one(browser):
    page = SimpleFormPage(browser, link)
    page.open()
    page.quest_one()


def test_quest_too(browser):
    page = SimpleFormPage(browser, link)
    page.open()
    page.quest_too()
