import items

def test_empty(item_db):
    assert item_db.count() == 0

def test_count(item_db):
    item_db.add_item(items.Item("something"))
    item_db.add_item(items.Item("something else"))
    assert item_db.count() == 2

def test_count2(item_db):
    item_db.add_item(items.Item("something different"))
    assert item_db.count() == 1

# def test_add_list(item_db, items_list):
#     expected_count = len(items_list)
#     for i in items_list:
#         item_db.add_item(i)
#     assert item_db.count() == expected_count