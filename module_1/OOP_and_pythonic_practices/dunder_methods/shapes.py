import math

class PositiveNumber:
    def __init__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self.name] = value
        
class CircleCopy:
    radius = PositiveNumber(owner='CircleCopy', name='radius')

    def __init__(self, radius):
        self.radius = radius

    def __area__(self):
        return round(math.pi * self.radius ** 2, 2)
    


class Square:
    side = PositiveNumber(owner='Square', name='side')

    def __init__(self, side):
        self.side = side

    def __area__(self):
        return round(self.side ** 2, 2)
    
class Rectangle:
    height = PositiveNumber(owner='Rectangle', name='height')
    width = PositiveNumber(owner='Rectangle', name='width')

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __area__(self):
        return self.height * self.width