import pytest
from playwright.sync_api import sync_playwright

from e2e.screenplay.actor import Actor
from e2e.screenplay.abilities import BrowseTheWeb

BASE_URL = "https://practicesoftwaretesting.com/"

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, slow_mo=2000, args=["--no-sandbow"])
        browser = p.chromium.launch(headless=True, args=["--no-sandbow"])
        context = browser.new_context(base_url=BASE_URL)
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def user(page):
    """Actor with the ability to surf the web (Playwright)."""
    actor = Actor("user")
    actor.can(BrowseTheWeb.using(page))
    return actor

