# tests/e2e/screenplay/interactions.py
from dataclasses import dataclass
from typing import Callable
from playwright.sync_api import Page
from e2e.screenplay.abilities import BrowseTheWeb

LocatorFactory = Callable[[Page], object]

@dataclass
class ClickRole:
    el: LocatorFactory
    def performed_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        self.el(page).click()

@dataclass
class FillInput:
    el: LocatorFactory
    value: int | float | str
    timeout: float | None = None

    def performed_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        loc = self.el(page)
        loc.wait_for(state="visible", timeout=self.timeout)
        text = f"{self.value}"
        loc.fill(text)

@dataclass
class Navigate:
    url: str  # relativa o absoluta
    def performed_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        page.goto(self.url)

@dataclass
class WaitFor:
    el: LocatorFactory
    state: str = "visible"
    timeout: float | None = None

    def performed_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        locator = self.el(page)
        locator.wait_for(state=self.state, timeout=self.timeout)

@dataclass
class SelectOption:
    el: LocatorFactory
    value: str | None = None

    def performed_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        locator = self.el(page)
        locator.select_option(value=self.value)