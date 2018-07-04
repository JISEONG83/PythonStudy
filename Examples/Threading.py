# Thread Examples
import threading
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print('sub-threading', total)

t = threading.Thread(target=sum, args=(1,50))
t.start()

print('Main-thread')

