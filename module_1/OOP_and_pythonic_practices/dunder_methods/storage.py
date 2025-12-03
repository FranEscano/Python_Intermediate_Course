class Storage(float):
    def __new__(cls, value, unit):
        instance =  super().__new__(cls, value)
        instance.unit = unit
        return instance
    
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand type for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        if not self.unit == other.unit:
            raise TypeError(
                f"incompatible unit: '{self.unit}' and '{other.unit}'"
            )
        return type(self)(super().__add__(other), self.unit)
             
    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand type for -: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        if not self.unit == other.unit:
            raise TypeError(
                f"incompatible unit: '{self.unit}' and '{other.unit}'"
            )
        return type(self)(super().__sub__(other), self.unit)
    
disk = Storage(1024, 'GB')

print(disk)
print(disk.unit)

isinstance(disk, float)  # True