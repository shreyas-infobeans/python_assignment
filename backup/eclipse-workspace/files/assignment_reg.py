import re
def contains_digits(str):
    pattern = r'\d'
    result = re.search(pattern,str)
    return result

str = input("Please enter any string")
print(contains_digits(str))