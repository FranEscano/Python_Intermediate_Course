# tests/e2e/screenplay/tasks.py
from dataclasses import dataclass

from e2e.screenplay.interactions import (ClickRole, Navigate, WaitFor, FillInput, SelectOption)
from e2e.screenplay.questions import (IsVisible, SeeTextContaining)
from e2e.screenplay.pages import home_page as Home
from e2e.screenplay.pages import product_page as Product
from e2e.screenplay.pages import checkout_page as CheckOut

@dataclass
class OpenHome:
    def performed_by(self, actor):
        actor.attempts_to(
            Navigate("/"),
            WaitFor(Home.home_logo)
        )

@dataclass
class GoToCategoriesAndFilterByHandTools:
    def performed_by(self, actor):
        actor.attempts_to(
            ClickRole(Home.hand_tools_filter)
        )

@dataclass
class ClickOnTheClawHammer:
    def performed_by(self, actor) :
        actor.attempts_to(
            ClickRole(Home.claw_hammer)
        )

@dataclass
class AddProductToTheCart:
    def performed_by(self, actor) :
        actor.attempts_to(
            ClickRole(Product.add_to_cart)
        )

@dataclass
class GoToTheCartUsingIcon:
    def performed_by(self, actor) :
        actor.attempts_to(
            ClickRole(Product.go_to_cart)
        )

@dataclass
class ChangeQuantityAndCheckout:
    def performed_by(self, actor) :
        actor.attempts_to(
            FillInput(CheckOut.fill_input, 5),
            ClickRole(CheckOut.proceed_checkout)
        )

@dataclass
class CountinueAsGuestAndInputDummyData:
    def performed_by(self, actor) :
        actor.attempts_to(
            ClickRole(CheckOut.continue_as_guest),
            FillInput(CheckOut.email_input, "dummy@email.com"),
            FillInput(CheckOut.first_name_input, "John"),
            FillInput(CheckOut.last_name_input, "Doe"),
            ClickRole(CheckOut.guest_submit),
            ClickRole(CheckOut.proceed_checkout),
            FillInput(CheckOut.street_input, "dummyStreet"),
            FillInput(CheckOut.city_input, "dummyCity"),
            FillInput(CheckOut.state_input, "dummyState"),
            FillInput(CheckOut.country_input, "dummyCountry"),
            FillInput(CheckOut.post_code_input, "duPoCo"),
            ClickRole(CheckOut.proceed_checkout),
        )

@dataclass
class PayWithCash:
    def performed_by(self, actor) :
        actor.attempts_to(
            SelectOption(CheckOut.payment_method, "Cash on Delivery"),
            ClickRole(CheckOut.confirm_button)
        )

@dataclass
class ConfirmPurchase:
    def performed_by(self, actor) :
        actor.should(
            IsVisible(CheckOut.successful_payment)
        ),
        actor.attempts_to(
            ClickRole(CheckOut.confirm_button)
        ),
        actor.should(
            SeeTextContaining(CheckOut.successful_payment)
        )