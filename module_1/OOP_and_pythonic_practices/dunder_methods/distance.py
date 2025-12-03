class Distance:
    _multiples = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        return self.value * type(self)._multiples[self.unit]
    
    def __add__(self, other):
        return self._compute(other, "+")
    
    def __sub__(self, other):
        return self._compute(other, "-")
    
    def _compute(self, other, operator):
        operation = eval(f"{self.to_meter()} {operator} {other.to_meter()}")
        cls = type(self)
        return cls(operation / cls._multiples[self.unit], self.unit)