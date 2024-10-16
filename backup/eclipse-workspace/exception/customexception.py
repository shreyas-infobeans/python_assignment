class OverTheLimit(Exception):
    def __init__(self,msg):
        self.msg = msg
        
        
def withdraw(amount):
    if(amount>500):
        raise OverTheLimit("You cannot enter more than 500")
    
withdraw(90)