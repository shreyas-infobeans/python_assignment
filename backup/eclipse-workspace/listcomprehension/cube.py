"""lst = []

for i in range(1,11):
    lst.append(i**3)
    
print(lst)"""

lst = []
lst = [x**3 for x in range(1,11)]
print(lst)