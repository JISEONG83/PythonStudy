
#Check item of Dict
def CheckDict(searchKeys, dict):
    print('dictionnay Collection : ', dict)
    print('search key value : ', searchKeys)
    if searchKeys in dict:
        print(dict[searchKeys])
    else:
        print("Not exist")

aDictExam1 = {'정지성':'a', '최종우':'b'}
print(aDictExam1)
print(aDictExam1['정지성'])
#print(aDictExam1[0])

# aDictExam2=dict(정지성=4,최종우=5) syntaxerror
aDictExam2=dict(a=4,b=5)
print(aDictExam2)
print(aDictExam2['a'])

aDictExam2['a'] = 10
print("Update dict -> ",aDictExam2)
aUpdateDict={'a':30, 'e':40}
aDictExam2.update(aUpdateDict)
print("Update All( update items =",aUpdateDict,") -> ", aDictExam2)
aDictExam2['c']=30

print("Append dict ->",aDictExam2)
del aDictExam2['c']
print("Delete dict ->",aDictExam2)
aDictExam2['d']=50


# keys
keys = aDictExam2.keys()
print('Keys : ')
for k in keys:
    print(k)
 
# values
print('Values: ')
values = aDictExam2.values()
for v in values:
    print(v)



# Search key
CheckDict('k', aDictExam2) # failed
CheckDict('a',aDictExam2) # success
