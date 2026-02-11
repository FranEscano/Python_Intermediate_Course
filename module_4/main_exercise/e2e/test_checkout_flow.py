import pytest

from screenplay.tasks import (OpenHome, GoToCategoriesAndFilterByHandTools, ClickOnTheClawHammer, AddProductToTheCart, GoToTheCartUsingIcon, ChangeQuantityAndCheckout, 
    CountinueAsGuestAndInputDummyData, PayWithCash, ConfirmPurchase)

def test_basic_checkout(user):
    user.attempts_to(
        OpenHome(),
        GoToCategoriesAndFilterByHandTools(),
        ClickOnTheClawHammer(),
        AddProductToTheCart(),
        GoToTheCartUsingIcon(),
        ChangeQuantityAndCheckout(),
        CountinueAsGuestAndInputDummyData(),
        PayWithCash(),
        ConfirmPurchase()
    )