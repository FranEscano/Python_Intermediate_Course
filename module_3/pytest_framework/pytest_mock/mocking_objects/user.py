class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def is_adult(self):
        return self.age >= 18