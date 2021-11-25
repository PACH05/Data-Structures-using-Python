#Enqueue and Dequeue operations in a Queue
from queue import LifoQueue , Queue

rq= Queue(maxsize=3)
rq.put(1)
rq.put(2)
rq.put(3)
print("Queue :")
print(rq.get())
print(rq.get())
print(rq.get())




   
    