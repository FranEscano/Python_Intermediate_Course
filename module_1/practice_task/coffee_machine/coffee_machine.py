def separator():
    separator = "-" * 60
    print(separator)

def add_coffee(func):
    def wrapper(*args, **kwargs):
        print("You add coffee")
        func(*args, **kwargs)
    return wrapper

def add_milk(func):
    def wrapper(*args, **kwargs):
        print("You add milk")
        func(*args, **kwargs)
    return wrapper

def add_sugar(func):
    def wrapper(*args, **kwargs):
        print("You add sugar")
        func(*args, **kwargs)
    return wrapper

@add_coffee
@add_milk
@add_sugar
def coffee_machine(coffee):
    print(f"Here is your {coffee}.")

coffee_machine("Capuccino")
separator()
coffee_machine("Latte")

separator()

@add_milk
@add_sugar
def custard():
    print("Here is your custard")

custard()