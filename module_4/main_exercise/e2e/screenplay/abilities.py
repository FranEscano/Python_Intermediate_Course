from playwright.sync_api import Page

class BrowseTheWeb:
    """Ability to use Playwright Page"""
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def using(page: Page) -> "BrowseTheWeb":
        return BrowseTheWeb(page)