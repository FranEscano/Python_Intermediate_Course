class Stack:
    def __init__(self, items=None):
        self._items = list(items) if items is not None else []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __contains__(self, item):
        for current_item in self._items:
            if current_item == item:
                return True
        return False
    
    def __add__(self, other):
        return type(self)(self._items + other._items)
    
    def __iadd__(self, other):
        self._items.extend(other._items)
        return self
    
    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"
    
    def __iter__(self):
        print("Iterating over stack:")
        return iter(self._items[::-1])  # LIFO order
    
    def __getitem__(self, index):
        print(f"Accessing item at index {index}")
        return self._items[index]
    
    def __len__(self):
        print("Getting length of stack")
        return len(self._items)
    
    def __reversed__(self):
        print("Reversing stack")
        return type(self)(reversed(self._items))