from playwright.sync_api import Page

def fill_input(page: Page):
    return page.locator('[data-test="product-quantity"]')

def proceed_checkout(page: Page):
    return page.get_by_role("button", name="Proceed to checkout")

def continue_as_guest(page: Page):
    return page.get_by_role("tab", name="Continue as Guest")

def email_input(page: Page):
    return page.locator('//*[@id="guest-email"]')

def first_name_input(page: Page):
    return page.get_by_placeholder("Your first name")

def last_name_input(page: Page):
    return page.get_by_placeholder("Your last name")

def guest_submit(page: Page):
    return page.locator('[data-test="guest-submit"]')

def street_input(page: Page):
    return page.get_by_placeholder("Your Street *")

def city_input(page: Page):
    return page.get_by_placeholder("Your City *")

def state_input(page: Page):
    return page.get_by_placeholder("State *")

def country_input(page: Page):
    return page.get_by_placeholder("Your country *")

def post_code_input(page: Page):
    return page.get_by_placeholder("Your Postcode *")

def payment_method(page: Page):
    return page.locator('select[data-test="payment-method"]')

def confirm_button(page: Page):
    return page.get_by_role("button", name=" Confirm ")

def successful_payment(page: Page):
    return page.locator('[data-test="payment-success-message"]')

def success_message(page):
    return page.get_by_text("Thanks for your order!")
