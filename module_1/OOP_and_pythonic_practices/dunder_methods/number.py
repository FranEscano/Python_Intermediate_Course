class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("__add__ called")
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        else:
            return TypeError("unsupported operand type for +")

    def __radd__(self, other):
        print("__radd__ called")
        return self.__add__(other)