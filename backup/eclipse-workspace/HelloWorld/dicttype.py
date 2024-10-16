dict1 = {1:"aaa",2:"bbb"}

print(dict1)

print(dict1.items())

k = dict1.keys()
for i in k:
    print(i)

v = dict1.values()
for i in v:print(i)

print(dict1[2])

del dict1[1]
print(dict1)