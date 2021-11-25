#Push and Pop operations in a Stack
from queue import LifoQueue
q= LifoQueue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
print("Stack")
print(q.get())
print(q.get())
print(q.get())