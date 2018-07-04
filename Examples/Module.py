# basic module

#import math
from math import factorial as f
#from math import (factorial, acos)
#from math import *
import sys
from myModules import *

#n = math.factorial(5)
#n = factorial(5)/factorial(3)
#n = factorial(5) - acos(1)
#n = factorial(5) - fabs(-12.5)
n = f(5) / f(2)
print(n)

# system path
print(sys.path)
print(sys.path[0])

# make module
i = add(10,20)
print(i)
i = substract(10,20)
print(i)


