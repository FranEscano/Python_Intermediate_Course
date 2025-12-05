def seperator():
    seperator = "-" * 40
    print(seperator)

if __name__ == "__main__":
    runners = ["Lenka", "Martina", "Gugu"]
    for winner in enumerate(runners):
        print(winner)

    seperator()

    for position, name in enumerate(runners):
        print(position, name)

    seperator()

    for position, name in enumerate(runners, start=1):
        print(position, name)

    seperator()

    tasks_by_priority = ("Pay Rent", "Clean Dishes", "Buy Milk")
    for index, task in enumerate(tasks_by_priority):
        if index == 0:
            print(f"* {task.upper()}!")
        else:
            print(f"* {task}")

    seperator()

    secret_message = "3LAigf7eq 5fhiOnpdDs2 Ra6 nwUalyo.9"
    message = ""
    for index, char in enumerate(secret_message):
        if index % 2:
            message += char

    print(message)

    seperator()

    lines = [
        "This is a\tline",
        "This line is fine",
        "Another line with whitespace "
    ]
    for lineno, line in enumerate(lines, start=1):
        if "\t" in line:
            print(f"Line {lineno}: Contains a tab charecter.")
        if line.rstrip() != line:
            print(f"Line {lineno}: Contains trailing whitespace.")