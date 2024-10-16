class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg = msg
def passcheck(password):
    if(len(password)<8):
        raise InvalidPasswordException("Password should be more than 8 characters")
try:
    password = input("Please enter the password:")
    passcheck(password)
except InvalidPasswordException as e:
    print(f"Password validation error: {e}")