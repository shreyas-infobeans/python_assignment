try:
    num = int(input("Please enter even number "))
    assert num%2==0, "You have entered invalid number"
except AssertionError as obj:
    print(obj)
    
print("After the assertion")