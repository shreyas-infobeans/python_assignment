class Duck:
    def talk(self):
        print("Quck Quck")
        
class Human:
    def talk(self):
        print("Hello")
        
def start(obj):
    obj.talk()
    
d = Duck()
h = Human()

start(d)
start(h)