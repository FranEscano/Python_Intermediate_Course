import pytest

@pytest.fixture()
def some_data():
    """The answer to the ultimate question"""
    return 42

def test_some_data(some_data):
    """Use fixture return valie in a test."""
    assert some_data == 42