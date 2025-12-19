import pytest

def test_db_initialised(item_db):
    if item_db.__class__.__name__ == "Sqlite":
        pytest.fail("Deliberately failing for demonstration purposes")