def separator():
    print("\n")

from person import Person

jane = Person("Jane Doe", 25)

str(jane)  # "I'm Jane Doe, and I'm 25 years old."

print(str(jane))  # I'm Jane Doe, and I'm 25 years old.
print(repr(jane))  # I'm John Doe, and I'm 35 years old.

john = Person("John Doe", 35)

john

repr(john)  # "Person(name=John Doe, age=35)"
print(str(john))  # I'm Jane Doe, and I'm 25 years old.
print(repr(john))  # I'm John Doe, and I'm 35 years old.

separator()

from storage import Storage

disk1 = Storage(500, 'GB')
disk2 = Storage(1000, 'GB')
disk3 = Storage(1, 'TB')

print(disk1 + disk2)  # 1500.0
# print(disk2 + disk3)  # Raises TypeError: incompatible unit: 'GB' and 'TB'
# print(disk1 + 100)  # Raises TypeError: unsupported operand type for +: 'Storage' and 'int'

print(disk1 - disk2)
# print(disk2 + disk3)
# print(disk1 + 100)

separator()

from distance import Distance

distance_1 = Distance(200, 'm')
distance_2 = Distance(1, 'km')

total = distance_1 + distance_2
print(total.value)
print(total.unit)

displacement = distance_2 - distance_1
print(displacement.value)
print(displacement.unit)

separator()

from number import Number

five = Number(5)
ten = Number(10)

fifteen = five + ten

six = five + 1

twelve = 2 + ten
print(fifteen.value)  # 15

print(six.value)  # 6

print(twelve.value)  # 12

separator()

from rectangle import Rectangle

basketball_court = Rectangle(15, 28)
football_field = Rectangle(75, 110)

print(basketball_court < football_field)  # True
print(basketball_court <= football_field)  # True
print(basketball_court == football_field)  # False
print(basketball_court != football_field)  # True
print(basketball_court > football_field)  # False
print(basketball_court >= football_field)  # False

separator()

print(2 in [2, 3, 4, 5, 9,7])  # True
print(10 in [2, 3, 4, 5, 9,7])

separator()

from stack import Stack

stack = Stack([2, 3, 4, 5, 9,7])

print(2 in stack)  # True
print(10 in stack)  # False 

print(2 not in stack)  # False
print(10 not in stack)  # True

separator()

from bitwise_number import BitwiseNumber

five = BitwiseNumber(5)  # binary: 0b101
ten = BitwiseNumber(10)  # binary: 0b1010

print(five & ten)  # Output: 0b0
print(five | ten)  # Output: 0b1111
print(five ^ ten)  # Output: 0b1111
print(~five)       # Output: -0b110
print(five << 2)  # Output: 0b10100
print(ten >> 1)   # Output: 0b101

separator()
stack = Stack([1, 2, 3])
stack += Stack([4, 5, 6])
print(stack)  # Stack([1, 2, 3, 4, 5, 6)

separator()
print(dir(Rectangle(12, 24)))  # Calls the custom __dir__ method

separator()
from circle import Circle
circle = Circle(10)
print(circle.radius)    # Triggers __getattribute__
print(circle.diameter)  # Triggers __getattr__

separator()

circle = Circle(10)

circle.radius = 20     # Valid assignment
# circle.radius = "42"  # Raises TypeError

circle.diameter = 42  # Raises AttributeError
print(circle.diameter)  # Triggers __getattr__

separator()
from non_deletable import NonDeletable

one = NonDeletable(1)
print(one.value)  # 1

# del one.value  # Raises AttributeError

separator()

from shapes import CircleCopy, Square, Rectangle
# circle = CircleCopy(-10)
# square = Square(-20)
# rectangle = Rectangle(-20, 30)

separator()

from fibonacci import FibonacciIterator

for fib_number in FibonacciIterator():
    print(fib_number) # Prints Fibonacci numbers up to the 10th number

separator()

from stack import Stack
stack = Stack([1, 2, 3, 4])
for value in stack:
    print(value)  # Prints 4, 3, 2, 1 in that order

separator()
from factorial import Factorial

factorial_of = Factorial()

print(factorial_of(4))  # 24
print(factorial_of(5))  # 120
print(factorial_of(6))  # 720

separator()
from stack import Stack

stack = Stack([1, 2, 3, 4])
print(stack[1])  # Accessing item at index 1
print(stack[-1])  # Accessing item at index -1
print(len(stack))  # Getting length of stack
print(reversed(stack))  # Reversing stack

separator()
from reader import TextFileReader

with open('hello.txt', mode='w', encoding="utf-8") as file:
    file.write("Hello, World!")
with open('hello.txt', mode='r', encoding="utf-8") as file:
    print(file.read())
    
with TextFileReader('hello.txt') as file:
    print(file.read())