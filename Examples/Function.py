# basic function shape
def sum(a, b):
    s = a + b
    return s

total = sum(4,7)
print(type(total))
print(total)

# input parameters
def f1(i, myList):
    i += 1
    myList.append(0)
    print('-- In the Function --')
    print(i)
    print(myList)
    print('-- In the Function --')

k = 10
m = [1,2,3]

f1(k, m)
print(k, m)

# default parameters
def f2(i, j, factor = 3):
    return i * j * factor

result = f2(10,20)
print(result)
result = f2(10,20,30)
print(result)

# named parameters
def f3(name, age, score):
    print(name, score)

f3(age=10, name="John", score=80)

# dynamic parameters
def f4(*numbers):
    print(type(numbers))
    total = 0
    for n in numbers:
        total += n
    return total

t = f4(1,2)
print(t)
t = f4(1,5,2,6)
print(t)

# return value
def f5(*numbers):
    count = 0
    total = 0
    for n in numbers:
        count += 1
        total += n
    return count, total

count, sum, = f5(1,5,2,6)
m = (1,2,3)
print('%d %d'%(count, sum))
print(count, sum)

