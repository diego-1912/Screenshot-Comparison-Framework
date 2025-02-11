import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    """
    Playwright fixture to launch a browser and provide a new page.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True if running in CI/CD
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
