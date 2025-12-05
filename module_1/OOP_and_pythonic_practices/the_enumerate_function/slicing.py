from enumerate import seperator
game_name = "Stardew Valley"
first_letters = ""
for i, letter in enumerate(game_name):
    if i < 4:
        first_letters += letter
    else:
        break

print(first_letters)

seperator()

print(game_name[:4])