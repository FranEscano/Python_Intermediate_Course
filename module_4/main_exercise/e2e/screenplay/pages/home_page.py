from playwright.sync_api import Page

def home_logo(page: Page):
    return page.locator("//html/body/app-root/app-header/nav/div/a")

def hand_tools_filter(page: Page):
    return page.get_by_role("checkbox", name="Hand Tools")

def claw_hammer(page: Page):
    return page.locator("//html/body/app-root/div/app-overview/div[3]/div[2]/div[1]/a[8]/div[1]/img")