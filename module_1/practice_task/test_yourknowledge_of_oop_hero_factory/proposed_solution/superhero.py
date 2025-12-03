class Superhero:
    def __init__(self, name, strength, speed, can_fly):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.can_fly = can_fly

    def __str__(self):
        if self.can_fly:
            flying_status = "and can fly"
        else:
            flying_status = "and cannot fly"
        return f"{self.name} has strength {self.strength}, speed {self.speed}, {flying_status}."
    
class Hulk(Superhero):
    def __init__(self, name, strength, speed, can_fly, special_ability):
        super().__init__(name, strength, speed, can_fly)
        self.special_ability = special_ability
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} Special ability: {self.special_ability}."
    
    def perform_ability(self):
        return f"{self.name} uses {self.special_ability}!"
    
hulk = Hulk(name="Hulk", strength=100, speed=80, can_fly=False, special_ability="Superhuman Strength")
print(hulk)
print(hulk.perform_ability())

class IronMan(Superhero):
    def perform_ability(self):
        return f"{self.name} using Repulsor Blast!"

ironMan = IronMan(name="Iron Man", strength=85, speed=90, can_fly=True)
print(ironMan)
print(ironMan.perform_ability())
