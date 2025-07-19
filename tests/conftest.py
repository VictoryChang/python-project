from playwright.sync_api import sync_playwright
import pytest

from tests.calculator_client import CalculatorClient

# api tests
@pytest.fixture(scope="session")
def client():
    return CalculatorClient()


# ui tests
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
