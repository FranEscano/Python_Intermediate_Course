def separator():
    separator = '=' * 60
    print(separator)

def fun(*args):
    return sum(args)

print(fun(5, 10, 15))

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

separator()
print("NON-KEYWORD ARGUMENTS (*ARGS)")
separator()

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))

separator()
print("KEYWORD ARGUMENTS (**KWARGS)")
separator()

def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')

def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="Alice", Age=25, City="New York"))

separator()
print("USING BOTH *ARGS AND **KWARGS")
separator()

def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Details:", kwargs)

student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")