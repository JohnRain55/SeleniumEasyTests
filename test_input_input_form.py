from .pages.input_forms.input_form_page import InputFormPage

link = "https://www.seleniumeasy.com/test/input-form-demo.html"


def test_should_be_elements(browser):
    page = InputFormPage(browser, link)
    page.open()
    page.should_be_elements()
