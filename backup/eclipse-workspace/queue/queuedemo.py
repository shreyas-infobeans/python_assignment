import queue

q = queue.Queue()
q.put("Python")
q.put("Django")
q.put("Angular")
print(q.queue)
q.queue.clear()
print(q.qsize())
while not q.empty():
    print(q.get())
print(q.qsize())