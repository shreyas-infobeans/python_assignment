class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg

age = int(input("Enter age: "))
if age<18:
    raise TooYoungException("You are too young")
elif age>90:
    raise TooOldException("Too old")
else:
    print("Eligible")