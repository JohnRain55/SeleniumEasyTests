from .pages.input_forms.jquery_select import JQuerySelectPage

link = "https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html"


def test_should_be_elements(browser):
    page = JQuerySelectPage(browser, link)
    page.open()
    page.should_be_elements()
