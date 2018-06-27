# Iterator
mylist = [1,2,3,4,5]
it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))

class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index=0
        return self

    def next(self):
        if self.index >= self.size:
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

coll = MyCollection()
for x in coll:
    print(x)

print('--------------------------')

#Generator
def gen():
    yield 1
    yield 2
    yield 3
g = gen()
print(type(g))
print(g)

n = next(g)
print(n)
n = next(g)
print(n)
n = next(g)
print(n)

for x in gen():
    print(x)

generator = (n*n for n in range(30))
print(type(generator))

convertedList = list(generator)
print('==')
for i in range(20):
    if i % 2 == 0:
        value = next(generator)
        print(value)

print('--')

for x in generator:
    print(x)

#print(convertedList)

