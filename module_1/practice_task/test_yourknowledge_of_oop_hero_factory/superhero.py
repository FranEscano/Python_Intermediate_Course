class Superhero:
    def __init__(self, name, strength, speed, flying):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.flying = flying

    def perform_ability(self, special_power ):
        return f"Using {special_power}!"
    
class Hulk(Superhero):
    def __init__(self, name, strength, speed, can_fly, special_ability):
        super().__init__(name, strength, speed, can_fly)
        self.special_ability = special_ability
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} Special ability: {self.special_ability}."
    
    def perform_ability(self):
        return f"{self.name} uses {self.special_ability}!"
    
class RedHulk(Hulk):
    def __init__(self, name, strength, speed, can_fly, special_ability, rage_level):
        super().__init__(name, strength, speed, can_fly, special_ability)
        self.rage_level = rage_level
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} Rage level: {self.rage_level}."
    
    def perform_ability(self):
        return f"{self.name} uses {self.special_ability} with rage level {self.rage_level}!"
    