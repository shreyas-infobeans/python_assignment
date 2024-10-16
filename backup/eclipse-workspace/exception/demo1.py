import logging

logging.basicConfig(filename="mylog.log",level=logging.ERROR)
try:
    f = open("file","w")
    a,b = [int(x) for x in input("Enter two numbers").split()]
    c = a/b
    f.write("Writing %d into file" %c)
    print(c)
except ZeroDivisionError:
    print("zero divisible not allowed")
    logging.error("This islog")
else:
    print("Numbers are correct")
finally:
    f.close()
    print("file close")
print("code after exception")