def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

print(my_generator())

for char in my_generator():
    print(char)

def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

for i in counter_generator(5,10):
    print(i, end=' ')

c = counter_generator(5, 10)
print(dir(c))

def infinite_generator(start=0):
    while True:
        yield start
        start += 1

for num in infinite_generator(4):
    print(num, end=' ')
    if num > 20:
        break

g = my_generator()
for c in g:
    print(c)

for c in g:
    print(c)

class Counter(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def __iter__(self):
        counter = self.low
        while self.high >= counter:
            yield counter
            counter += 1

gobj = Counter(5,10)
for num in gobj:
    print(num, end=' ')
    
for num in gobj:
    print(num, end=' ')