queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)


queue.pop(0)
queue.pop(0)
queue.pop(0)

print(queue)

from collections import deque

a= deque()

a.append(1)
a.append(2)
a.append(3)
print("second queue is ", a)

a.popleft()
a.popleft()
print("afterpop", a)

# from python queue.Queue
"""Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. """
from queue import Queue

b = Queue(maxsize=3)
b.put("a")
b.put("3")

b.get()
print(" b is", b)
