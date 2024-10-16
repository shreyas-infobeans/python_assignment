s = input("Enter a sentense ")
temp = s.split()
print(temp)
result = []
i = 0

while i<  len(temp):
    result.append(temp[i][::-1])
    i= i + 1
    
output = ''.join(result)
print(output)