def my_fucntion():
    print("Hello world!")

def greeter():
    print("Hello from mymodule!")

# Only call the greeter when run as
# a script (with python mymodule.py)
if __name__ == "__main__":
    greeter()