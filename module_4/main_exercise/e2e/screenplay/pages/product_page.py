from playwright.sync_api import Page

def add_to_cart(page: Page):
    return page.get_by_role("button", name="Add to cart ")

def go_to_cart(page: Page):
    return page.locator('[data-test="nav-cart"]')