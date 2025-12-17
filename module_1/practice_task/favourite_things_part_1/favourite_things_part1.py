def favourite_things(*args):
    for index, value in enumerate(args, start=1):
        verb = "is"
        if value.endswith("s"):
            verb = "are"

        if index == 1:
            print(f"One of my favourite things {verb} {value}")
        else:
            print(f"Another of my favourite things {verb} {value}")

    print(f"These are {index} of my favourite things")
    
favourite_things("chocolate", "videogames", "holidays", "relaxing")