max_size = 10

# Print function
def printIter(iter, size):
    outputStr=""
    for n in range(size):
        outputStr+=str(next(iter)) + '\t'
    print(outputStr)


#iterator expr
ItemList = []
for i in range(max_size):
    ItemList.append(i)
#initialize iterator
a_iter = iter(ItemList)

outputStr=""
for n in range(max_size):
    outputStr+=str(next(a_iter)) + '\t'
print(outputStr)


#Iterator Exam
class iterCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))
 
    def __iter__(self):
        self.index = 0
        return self
 
    def next(self): # when use the python 2 version
        if self.index >= self.size:
            raise StopIteration
 
        n = self.data[self.index]
        self.index += 1
        return n
 
 
coll = iterCollection()
for x in coll:
    print(x)



print('-------------------------------------')
#Generator expr
g = (i for i in range(max_size))
print(g)

printIter(g, max_size)


print('-------------------------------------')

# geneator function
def gen():
    def reset():
        return 0;
    i=reset()
    val = 0
    while True:
        val = (yield i)
        if val == "reset" :
            i = reset()
            yield i
        else:
            i=i+1
                
# Generator to Iterator
g = gen()
printIter(g,max_size)
g.send("reset")
printIter(g,max_size)






