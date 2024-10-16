from threading import *
import threading

class EvenNumberThread:
    def run(self):
        for i in range(1,100):
            if(i%2==0):
                print(i)
                
obj = EvenNumberThread()
t = Thread(target=obj.run)
t.start()

class OddNumberThread:
    def run(self):
        for i in range(1,100):
            if(i%2 != 0):
                print(i)
                
obj1 = OddNumberThread()
t1 = Thread(target=obj1.run)
t1.start()

print("Current running thread ",threading.current_thread().getName())

if(threading.current_thread()==threading.main_thread()):
    for i in range(1,100):
        print(i)    
    