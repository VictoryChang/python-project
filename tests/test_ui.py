from playwright.sync_api import Page


def test_sum(page: Page):
    page.goto("http://127.0.0.1:8000/ui/v1/sum?a=1&b=2")
    value = page.locator('//div[@name="sum"]').text_content()
    assert value == "3"


def test_double_sum(page: Page):
    page.goto("http://127.0.0.1:8000/ui/v1/double_sum?a=1&b=2")
    value = page.locator('//div[@name="double_sum"]').text_content()
    assert value == "6"
