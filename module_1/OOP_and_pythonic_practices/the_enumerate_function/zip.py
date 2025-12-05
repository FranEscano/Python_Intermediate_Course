from enumerate import seperator

pets = ["Leo", "Aubrey", "Frieda"]
owners = ["Bartosz", "Sarah Jane", "Philipp"]

for i, pet in enumerate(pets):
    print(f"{pet} & {owners[i]}")

seperator()

for pet, owner in zip(pets, owners):
        print(f"{pet} & {owner}")
