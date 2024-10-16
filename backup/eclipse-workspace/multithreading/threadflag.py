from threading import *
from time import *


class producer:
    def __init__(self):
        self.products = []
        self.orderedplaced = False
    def produce(self):
        for i in range(1,5):
            self.products.append("product"+str(i))
            sleep(1)
            print("Item added")
        self.orderedplaced = True

class Consumer:
    def __init__(self,prod):
        self.prod = prod
        
    def consume(self):
        while self.prod.orderedplaced == False:
            sleep(0.2)
        print("Shipped",self.prod.products)
        


P = producer()
C = Consumer(P)

t1 = Thread(target=P.produce)
t2 = Thread(target=C.consume)

t1.start()
t2.start()


        