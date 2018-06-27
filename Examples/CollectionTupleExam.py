import random

max_size = 10

#Create Tuple
aTuple=(1,"a","jeong")
print(type(aTuple))
print(aTuple)
print(aTuple[1])

# Dynamic Tuple by Generator
aList2=[]
g = ( random.randrange(1,max_size) for i in range(max_size))
for i in range(max_size):
    aList2.append(next(g))
aTuple2 = tuple(aList2)
print("Tuple Values = " + str(aTuple2))

#Tuple Slicing
randStartIdx = random.randrange(-max_size, max_size)
randLastIdx = random.randrange(0,max_size)
slicingTuple = aTuple2[randStartIdx:randLastIdx]
print("Tuple StartIndex=["+str(randStartIdx)+"], Tuple length = ["+str(randLastIdx)+"] ->  Values : "+str(slicingTuple))


# update values(Tuple does not change value)
aCopyTuple2=aTuple2
#aCopyTuple2[randStartIdx] = "asdfasdf" ## Occurred TypeError exception. 
print(aTuple2)

#Tuple Index and Count
r = random.randrange(1,max_size)
i = aTuple2.index(r)
c = aTuple2.count(r)
outputstr = "random number = "+str(r)
outputstr += ",first index = "+str(i)
outputstr += ",count of number("+str(r)+") = "+ str(c)
print(outputstr)

#Tuple Comprehension
aTuple3 = tuple(random.randrange(1,max_size) for i in range(max_size))
print("Tuple Values = " + str(aTuple3))