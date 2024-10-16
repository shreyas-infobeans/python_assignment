try:
    a,b = [int(x) for x in input("Enter two numbers").split()]
    c = a/b
    print(c)
except ZeroDivisionError:
    print("zero divisible not allowed")
print("code after exception")