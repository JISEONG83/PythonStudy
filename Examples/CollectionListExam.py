import random

max_size = 10

#Create List
aList=[1,"a","jeong"]
print(aList)
print(aList[1])

# Dynamic List by Generator
aList2=[]
g = ( random.randrange(1,max_size) for i in range(max_size) )
for i in range(max_size):
    aList2.append(next(g))
print("List Values = " + str(aList2))


#List Slicing
randStartIdx = random.randrange(-max_size, max_size)
randLastIdx = random.randrange(0,max_size)
slicingList = aList2[randStartIdx:randLastIdx]
print("List StartIndex=["+str(randStartIdx)+"], List LastIndex = ["+str(randLastIdx)+"] ->  Values : "+str(slicingList))


# update values(Tuple does not change value)
aCopyList2=aList2
aCopyList2[randStartIdx] = "asdfasdf"
print(aList2)

#List Index and Count
r = random.randrange(1,max_size)
i = aList2.index(r)
c = aList2.count(r)
outputstr = "random number = "+str(r)
outputstr += ",first index = "+str(i)
outputstr += ",count of number("+str(r)+") = "+ str(c)
print(outputstr)

#List Comprehension
aList3 = [random.randrange(1,max_size) for i in range(max_size)]
print("List Values = " + str(aList3))