try:
    lst = [10,20,30,40,50,60]
    i = int(input(f"Enter index between 0 {len(lst)-1}"))
    print("Value in that index is:",lst[i])
except IndexError:
    print("value beyond index")