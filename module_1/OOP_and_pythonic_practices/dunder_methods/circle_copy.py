import math

class CircleCopy:
    def __init__(self, radius):
        self.radius = radius

    def __getattribute__(self, name):
        print(f"__getattribute__ called for {name}")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        if name == "diameter":
            return self.radius * 2
        return super().__getattr__(name)
    
    def __setattr__(self, name, value):
        print(f"__setattr__ called for {name}")
        if name == "radius":
            if not isinstance(value, int | float):
                raise TypeError("Radius must be a number.")
            if value <= 0:
                raise ValueError("Radius must be positive.")
        super().__setattr__(name, value)