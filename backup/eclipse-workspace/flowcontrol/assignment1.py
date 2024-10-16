val = int(input("Enter a number"))
primeflag = True
"""for i in range(1,val+1):
    if(i%10==0):
        continue
    if(i>=100):
        break
    print(i)"""
for i in range(2,val):
    if(val%i==0):
        primeflag = False;
if(primeflag):
    print("Prime No")
else:
    print("Not a prime no")