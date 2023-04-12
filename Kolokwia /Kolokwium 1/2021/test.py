from queue import PriorityQueue

q = PriorityQueue()

q.put(-10)
q.put(-13)
q.put(-2)

print(-q.get())
