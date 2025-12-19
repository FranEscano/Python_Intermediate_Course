import pytest
from items import Item

def test_equality_fails():
    i1 = Item("do something", "veit")
    i2 = Item("do something else", "veit.schiele")
    if i1 != i2:
        pytest.fail("The items are no identical!")

if __name__ == "__main__":
    test_equality_fails()