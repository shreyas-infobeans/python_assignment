import queue

lq = queue.LifoQueue()
lq.put("A")
lq.put("B")
lq.put("C")
lq.put("D")
print(10>20)
print(lq.queue)

while not lq.empty():
    print(lq.get())