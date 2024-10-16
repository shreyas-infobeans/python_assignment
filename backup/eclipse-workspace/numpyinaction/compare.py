from numpy import *

a1 = array([100,30,3,4,5])

a2 = array([20,40,4999,1,3])

#print(a1>a2)

#print(any(a1>a2))

#print(all(a1>=a2))

#print(logical_and(a1>410,a1<101))
#print(logical_or(a1>410,a1<101))

print(where(a1%2!=0,a1,0))

print(where(a1>a2,a1,a2))