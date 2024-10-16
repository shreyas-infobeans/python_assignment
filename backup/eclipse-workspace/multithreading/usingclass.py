from threading import *
from time import sleep

class MyT:
    def run(self):
        i=0
        print(current_thread().getName())
        sleep(1)
        while(i<10):
            print(i)
            i+=1
obj = MyT()
t = Thread(target=obj.run)
t.start()

t1 = Thread(target=obj.run)
t1.start()

t2 = Thread(target=obj.run)
t2.start()