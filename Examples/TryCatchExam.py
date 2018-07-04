# TryCatch Exam 1( Call function)
def AppendSet(first, second):
    try:
        result = first.copy()
        result.update(second)
    except TypeError as err:
        print(err)
    else:
        print("no exist error")
        print("1st-parameter = ",first)
        print("2nd-parameter = ",second)
    finally:
        return result

set1={0,1,4,5}
#set2={0,1,6} # no error
set2=4
print("Result Set Collection = ", AppendSet(set1,set2))