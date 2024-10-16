lst1 = [2,0,3,4,5]
lst2 = [10,20,5,30,0]
lst3 = []
'''for i in range(len(lst1)):
    lst3.append(lst1[i]*lst2[i])'''
#lst3 = [lst1[i]*lst2[i] for i in range(len(lst1))]

'''for i in range(len(lst1)):
    if lst1[i] in lst2:
        lst3.append(lst1[i])'''
        
#lst3 = [lst1[i] for i in range(len(lst1)) if lst1[i] in lst2]
lst3 = [i for i in lst1 if i in lst2]
print(lst3)