f = open("myfile.txt","w")
print("Enter text type # when done")
s = ''
while s!='#':
    s= input()
    f.write(s+"\n")
f.close