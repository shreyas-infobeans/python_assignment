from threading import *
from time import *


class producer:
    def __init__(self):
        self.products = []
        self.c = Condition()
    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("product"+str(i))
            sleep(1)
            print("Item added")
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self,prod):
        self.prod = prod
        
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print("Shipped",self.prod.products)
        


P = producer()
C = Consumer(P)

t1 = Thread(target=P.produce)
t2 = Thread(target=C.consume)

t1.start()
t2.start()


        