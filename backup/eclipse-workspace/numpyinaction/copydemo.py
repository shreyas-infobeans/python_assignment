from numpy import *

a1  = arange(1,10)
a2 = a1.view()

a2 = a1.copy()

print("a1",a1)
print("a2",a2)