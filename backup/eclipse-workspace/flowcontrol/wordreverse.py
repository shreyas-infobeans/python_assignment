s = "All the power is within you"
temp = s.split()
print(temp)
res = []
i = len(temp)-1

while i>=0:
    res.append(temp[i])
    i=i-1
    
print(res)
output = ' '.join(res)
print(output)