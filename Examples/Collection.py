import numpy as np
# List
a = [ ]
print(type(a))
print(a)

print("--------------------")

a = ["AB", 10, False]
print(type(a))
print(a)

print("--------------------")

x = a[0]
print(x)
x = a[1]
print(x)
print(a[-3])

print("--------------------")

b = [1,2,3,4,5,6,7,8,9,10]
print(b)
y = b[2:5]
print(y)
y = b[2:]
print(y)
y = b[:5]
print(y)

print("--------------------")

b.append(20)
print(b)
b[2] = 100
print(b)
del b[1]
print(b)

print('--------------------')

c = a + b
print(c)
d = a * 3
print(d)

print('--------------------')

i = c.index('AB')
print(i)
ii = d.count('AB')
print(ii)

print('--------------------')

list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)
print(type(list))

print('--------------------')

matrix = [[ 0 for col in range(10)] for row in range(10)]
print(matrix)
matrix1 = [[0]*10]*10
print(matrix1)
matrix[0][0] = 1
print(matrix)
matrix1[1][1] = 1
print(matrix1)

matrix2 = np.random.randint(-20, 20, size=(5,5))
print(matrix2)

print('---------------------')

# tuple
t = ('AB', 10, False)
print(type(t))
print(t)

table = ('John', 'Blue')
print(table)
Name, Char = ('John', 'Blue')
print(Name, Char)
print(table[1])

print('---------------------')

# dictionary
scores = {'a' : 80, 'b' : 90, 'c': 20} # space check
print(type(scores))
print(scores)
scores['a'] = 100
scores['d'] = 300
print(scores)
del scores['c']
print(scores)
scores_keys = scores.keys()
print(scores_keys)
scores_values = scores.values()
print(scores_values)
scores_items = scores.items()
print(scores_items)

print('---------------------')

# set
myset = { 1, 1, 3, 5, 5}
print(type(myset))
print(myset)
mylist = [ 'AB', 'CD', 'EF']
print(mylist)
print(set(mylist))
myset.add(7)
print(myset)
myset.update({2,4,6})
print(myset)
myset.clear()
print(myset)

SetA = {1,3,5}
SetB = {2,3,5,6}
i = SetA & SetB
print(i)
ii = SetA|SetB
print(ii)
iii = SetA - SetB
print(iii)
iiii = SetB - SetA
print(iiii)

