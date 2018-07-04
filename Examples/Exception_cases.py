# Exceptions

def calc(values):
    sum = None

    try:
        sum = values[0] + values[1] + values[2]
#    except IndexError as err:
#        print('Index Error')
#    except Exception as err:
#        print(str(err))
    except (IndexError, Exception):
        print('Exception Thrown')
    else:
        raise Exception('normal, not error')
        #print('No Error')
    finally:
        print(sum)

calc([1,2,4,6])
#calc([1,2]

