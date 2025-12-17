def favourite_things(*args, **kwargs):
    print(f"Here are my top {len(kwargs)} favourite things")
    print("---")

    for k, val in kwargs.items():
        print(f"{k}: {val}")

    print("---")

    print("Some of my other favourite things are:")
    for index, value in enumerate(args):
        if index == len(args) -1:
            print(f"and {value}")
        else:
            print(value)

favourite_things("chocolate", "kittens", "music", "movies", First="Pizza", Second="Watching TV", Third="Spending time with loved ones", Forth="Basketball")