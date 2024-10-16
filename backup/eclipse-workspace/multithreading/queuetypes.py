import queue

''''q= queue.Queue()
q.put(100)
q.put(200)
q.put(400)

while not q.empty():
    print(q.get(),end=' ')'''
    
    
pq= queue.PriorityQueue()
pq.put((100,"res"))
pq.put((200,"def"))
pq.put((400,"opi"))

while not pq.empty():
    print(pq.get()[1],end=' ')