def calc(a,b,operation):
    if operation==1:
        return a+b
    if operation==2:
        return a-b  
    if operation==3:
        return a*b  
    if operation==4:
        return a/b      
a,b = [int(x) for x in input("Please enter two numbers: ").split()]
print(a)
print(b)
operation = int(input("Select respective digit mentioned in bracket to perform operations \n1.Sum(1) \n2.Substraction(2) \n3.Multiplication(3) \n4.Division(4) "))
print(operation)
result = calc(a,b,operation)
print("Result is: ",result)