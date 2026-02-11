# tests/e2e/screenplay/questions.py
from dataclasses import dataclass
from typing import Callable
from playwright.sync_api import Page, expect

from e2e.screenplay.abilities import BrowseTheWeb

LocatorFactory = Callable[[Page], object]

@dataclass
class SeeTextContaining:
    el: Callable[[Page], object]
    
    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        expect(self.el(page)).to_be_visible()

@dataclass
class IsVisible:
    el: LocatorFactory
    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        expect(self.el(page)).to_be_visible()