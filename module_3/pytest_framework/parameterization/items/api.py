from dataclasses import dataclass, field

from .db import DB

@dataclass
class Item:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

class ItemsException(Exception):
    pass

class ItemsDB:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, ".items_db")
        self._items = []

    def add_item(self, item: Item):
        self._items.append(item)
        return len(self._items) - 1
    
    def count(self):
        return len(self._items)
    
    def get_item(self, item_id: int):
        return self._items[item_id]
    
    def update_item(self, item_id: int, item:Item):
        existing = self._items[item_id]
        for field in ("summary", "owner", "state"):
            value = getattr(item, field)
            if value is not None:
                setattr(existing, field, value)
    
    def delete_item(self, item:Item):
        return
    
    def delete_all(self):
        self._items.clear()
    
    def close(self):
        self._db.close()

    def path(self):
        return self._db_path
    
    def finish(self, item_id: int):
        """Set an item state to done."""
        self.update_item(item_id, Item(state="done"))