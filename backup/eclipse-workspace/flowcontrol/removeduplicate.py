l1 = eval(input("Please enter list of elements "))
print(l1)
l3 = set(l1)
print(l3)
l2 = []

for each_value in l1:
    if(each_value not in l2):
        l2.append(each_value)
print(l2)    

