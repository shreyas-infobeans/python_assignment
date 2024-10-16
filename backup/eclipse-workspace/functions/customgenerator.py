def custom(x,y):
    while x<y:
        yield x
        x+=1
        
result = custom(20,30)

#print(result)

for i in result:
    print(i)