# Exception - file

# popular format
#try:
#    fp = open('text.txt', 'r')
#    try:
#        lines = fp.readlines()
#        print(lines)
#    finally:
#        fp.close()
#    except IOError:
#        print('File Error')

# using with
with open('text.txt', 'r') as fp:
    lines = fp.readlines()
    print(lines)

