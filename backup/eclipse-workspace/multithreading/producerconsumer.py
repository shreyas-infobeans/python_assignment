import random
import time
import queue
from threading import *

def producer(q):
    while True:
        print("producing")
        q.put(random.randint(1,50))
        print("Produced")
        time.sleep(3)
        
def consumer(q):
    while True:
        print("Ready to consume")
        print("Consumedata",q.get())
        time.sleep(3)

q = queue.Queue()
t1 = Thread(target=consumer,args=(q,))
t2 = Thread(target=producer,args=(q,))

t1.start()
t2.start()