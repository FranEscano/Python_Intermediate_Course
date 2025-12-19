from items import Item
import pytest

def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in progress", "todo"])
        
# @pytest.fixture(params=["done", "in progress", "todo"])
# def start_state(request):
#     return request.param

# @pytest.mark.parametrize(
#         "start_summary, start_state",
#         [
#             ("Update cibuildwheeel section", "done"),
#             ("Update pytest section", "in progress"),
#             ("Update mock tests", "todo"),
#         ],
# )

# @pytest.mark.parametrize(
#         "start_state",
#         [
#             ("done"),
#             ("in progress"),
#             ("todo"),
#         ],
# )

# def test_finish_from_in_prog(item_db):
#     index = item_db.add_item(
#         Item("Update pytest section", state="in progress")
#     )
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

# def test_finish_from_done(item_db):
#     index = item_db.add_item(
#         Item("Update cibuildwheeel section", state="done")
#     )
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

# def test_finish_from_todo(item_db):
#     index = item_db.add_item(Item("Update mock tests", state="todo"))
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

# def test_finish(item_db):
#     for i in [
#         Item("Update cibuildwheeel section", state="done"),
#         Item("Update pytest section", state="in progress"),
#         Item("Update mock tests", state="todo"),
#     ]:
#         index = item_db.add_item(i)
#         item_db.finish(index)
#         item = item_db.get_item(index)
#         assert item.state == "done"

# def test_finish(item_db, start_summary, start_state):
#     initial_item = Item(summary=start_summary, state=start_state)
#     index = item_db.add_item(initial_item)
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

# def test_finish(item_db, start_state):
#     i = Item("Update pytest section", state=start_state)
#     index = item_db.add_item(i)
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

# def test_finish(item_db, start_state):
#     i = Item("Update pytest section", state=start_state)
#     index = item_db.add_item(i)
#     item_db.finish(index)
#     item = item_db.get_item(index)
#     assert item.state == "done"

def test_finish(item_db, start_state):
    i = Item("Update pytest section", state=start_state)
    index = item_db.add_item(i)
    item_db.finish(index)
    item = item_db.get_item(index)
    assert item.state == "done"