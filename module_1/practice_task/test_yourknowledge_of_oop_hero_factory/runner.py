from superhero import Superhero, Hulk, RedHulk

separator = "-" * 40

hulk = Superhero(name="Hulk", strength=100, speed=80, flying=False)
print(f"{hulk.name} strength is {hulk.strength}")  # 100
print(f"{hulk.name} speed is {hulk.speed}")     # 80
print(f"Can {hulk.name} fly? {hulk.flying}")    # False
print(hulk.perform_ability("Superhuman Strength"))  # Using super strength!

print(separator)

ironMan = Superhero(name="Iron Man", strength=85, speed=90, flying=True)
print(f"{ironMan.name} strength is {ironMan.strength}")  # 85
print(f"{ironMan.name} speed is {ironMan.speed}")     # 90
print(f"Can {ironMan.name} fly? {ironMan.flying}")    # True
print(ironMan.perform_ability("Repulsor Blast"))  # Using flight!

print(separator)

captainAmerica = Superhero(name="Captain America", strength=70, speed=75, flying=False)
print(f"{captainAmerica.name} strength is {captainAmerica.strength}")  # 70
print(f"{captainAmerica.name} speed is {captainAmerica.speed}")     # 75
print(f"Can {captainAmerica.name} fly? {captainAmerica.flying}")    # False
print(captainAmerica.perform_ability("Shield Throw"))  # Using shield throw!

print(separator)

thor = Superhero(name="Thor", strength=95, speed=85, flying=True)
print(f"{thor.name} strength is {thor.strength}")  # 95
print(f"{thor.name} speed is {thor.speed}")     # 85
print(f"Can {thor.name} fly? {thor.flying}")    # True
print(thor.perform_ability("Thunder Strike"))  # Using thunder strike!

print(separator)

blackWidow = Superhero(name="Black Widow", strength=60, speed=95, flying=False)
print(f"{blackWidow.name} strength is {blackWidow.strength}")  # 60
print(f"{blackWidow.name} speed is {blackWidow.speed}")     # 95
print(f"Can {blackWidow.name} fly? {blackWidow.flying}")    # False
print(blackWidow.perform_ability("Martial Arts"))  # Using martial arts!

print(separator)

hawkeye = Superhero(name="Hawkeye", strength=65, speed=85, flying=False)
print(f"{hawkeye.name} strength is {hawkeye.strength}")  # 65
print(f"{hawkeye.name} speed is {hawkeye.speed}")     # 85
print(f"Can {hawkeye.name} fly? {hawkeye.flying}")    # False
print(hawkeye.perform_ability("Archery"))  # Using archery!

red_hulk = RedHulk(name="Red Hulk", strength=110, speed=75, can_fly=False, special_ability="Enhanced Strength", rage_level=10)
print(red_hulk)
print(red_hulk.perform_ability())