class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __le__(self, other):
        return self.area() <= other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __ne__(self, other):
        return self.area() != other.area()
    
    def __ge__(self, other):
        return self.area() >= other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __dir__(self):
        print("__dir__ called")
        return sorted(self.__dict__.keys())