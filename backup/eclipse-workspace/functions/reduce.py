from functools import reduce
lst = [3,4,5]

fn = reduce(lambda x,y:x+y, lst)

print(fn)