import threading
print("Current running thread ",threading.current_thread().getName())

if(threading.current_thread()==threading.main_thread()):
    print("in main")