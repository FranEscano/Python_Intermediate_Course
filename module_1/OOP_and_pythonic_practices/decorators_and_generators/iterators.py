class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        print("Returns itseld as an iterator object")
        return self
    
    def __next__(self):
        print("Returns the next value till current is lower that high")
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
        
c = Counter(5,10)
for i in c:
    print(i, end=' ')

c = Counter(5,6)
next(c)
next(c)
# next(c)

iterator = iter(c)
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break