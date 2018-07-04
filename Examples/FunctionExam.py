# Function Exam 1( Call function)
def AppendSet(first, second):
    if isinstance(first, set) == False or isinstance(second, set) == False:
        print("parameter is not set collection.")
        return None
    print("1st-parameter = ",first)
    print("2nd-parameter = ",second)
    result = first.copy()
    result.update(second)
    return result

set1={0,1,4,5}
set2={0,1,6}
print("Result Set Collection = ", AppendSet(set1,set2))


# Function Exam 2 ( Compare to mutable param and immutable param)
print('\nFunction Exam 2 ( Compare to mutable param and immutable param)')
def AddCollectionList(aList, i):
    i = i+1
    print('update value inside function = '+str(i))
    if isinstance(aList,list) == True: # alist is collection list
        aList.append(i)
        return aList
    else:
        resultlist=[]
        resultlist.append(aList, i)
        return resultlist

def printvalue(title,aList,i):
    print(title)
    print("Mutable value ="+str(aList))
    print("Immutable value ="+str(i))

aItems=[1,2,3,4,5]
aVar = 9
print('-----------------')
printvalue('Before Call function', aItems, aVar)
print('-----------------')
AddCollectionList(aItems, aVar)
print('-----------------')
printvalue('after Call function', aItems, aVar)

# Function Call Exam 3(Default + named paramerters)

print('\nFunction Call Exam 3(Default + named paramerters)')
def Sum (ListParams, step= 1 ):
    total = 0
    if isinstance(ListParams, list) == True:
        for i in ListParams[::step]:
            total = total + i
    return total

def Sum2 (*VarParams ):
    total = 0
    for i in range(VarParams):
        total = total + i
    return total

print(Sum(step=2 ,ListParams = [1,2,3,4,5]))