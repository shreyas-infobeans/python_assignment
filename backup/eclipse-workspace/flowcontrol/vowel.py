word = input("Please enter any word: ")
result = {}
vowels = {"a", "e", "i", "o", "u"}

for c in word:
    if c in vowels:
        result[c] = result.get(c,0)+1
        
for k,v in result.items():
    print(k, "present ", v, "times")