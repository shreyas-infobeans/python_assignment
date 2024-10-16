from numpy import *

a1 = arange(12)

print('a1',a1)

a2 = reshape(a1,(2,6))

print('a2',a2)

print(a2.flatten())

print(eye(2))