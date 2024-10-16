from threading import *

class Mybus:
    def __init__(self,availableseats):
        self.availableseats = availableseats
        self.l = Lock()
        
    def buy(self,requestedseats):
        self.l.acquire()
        print("total seats:",self.availableseats)
        if(requestedseats<self.availableseats):
            print("Booking ticket")
            print("Making Payment")
            print("Printing ticket")
            self.availableseats -= requestedseats
        else:
            print("Sorry no seats")
        self.l.release()
obj = Mybus(10)
t = Thread(target=obj.buy,args=(3,))


t1 = Thread(target=obj.buy,args=(3,))


t2 = Thread(target=obj.buy,args=(3,))

t.start()
t1.start()
t2.start()