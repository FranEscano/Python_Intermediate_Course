import pytest
from tempfile import TemporaryDirectory
from pathlib import Path
import items
import os

@pytest.fixture(autouse=True, scope="session")
def setup_test_env():
    found = os.environ.get("APP_ENV", "")
    os.environ["APP_ENV"] = "TESTING"
    yield
    os.environ["APP_ENV"] = found

def db_scope(fixture_name, config):
    if config.getoption("--fdb", None):
        return "function"
    return "session"

@pytest.fixture(scope=db_scope)
def db():
    """ItemsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = items.ItemsDB(db_path)
        yield db
        db.close()


@pytest.fixture(scope="function")
def item_db(db):
    """ItemsDB object that's empty"""
    db.delete_all()
    return db

@pytest.fixture(scope="session")
def items_list():
    """List of different Item objects"""
    return [
        items.Item("Add Python 3.12 static type improvements", "veit", "todo"),
        items.Item("Add tips for efficient testing", "veit", "wip"),
        items.Item("Update cibuildwheel section", "veit", "done"),
        items.Item("Add backend examples", "veit", "done")
    ]

@pytest.fixture(scope="function")
def populated_db(item_db, items_list):
    """ItemsDB object populated with 'items_list'"""
    for i in items_list:
        item_db.add_item(i)
    return item_db

def pytest_addoption(parser):
    parser.addoption(
        "--fdb",
        action="store_true",
        default=False,
        help="Create new db for each test",
    )

#===========================================================#
#             TEST_BACKEND
#===========================================================#
def pytest_generate_tests(metafunc):
    if "item_db" in metafunc.fixturenames:
        metafunc.parametrize("item_db", ["json", "sqlite"], indirect=True)

class Json:
    "JSON object"

class Sqlite:
    "Sqlite database object"

@pytest.fixture
def item_db(request):
    if request.param == "json":
        return Json()
    elif request.param == "sqlite":
        return Sqlite()
    else:
        raise ValueError("Invalid internal test config")