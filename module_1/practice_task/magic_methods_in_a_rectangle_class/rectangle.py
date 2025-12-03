class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width = {self.width}, height = {self.height})"
    
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)
    
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)

print(rect1)
print(rect2)
print(rect1 + rect2)