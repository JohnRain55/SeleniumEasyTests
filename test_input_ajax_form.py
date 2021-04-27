from .pages.input_forms.ajax_form_page import AjaxFormPage

link = "https://www.seleniumeasy.com/test/ajax-form-submit-demo.html"


def test_should_be_elements(browser):
    page = AjaxFormPage(browser, link)
    page.open()
    page.should_be_elements()

#
# def test_should_submit_only_with_name(browser):
#     page = AjaxFormPage(browser, link)
#     page.open()
#     page.should_submit_only_with_name()
