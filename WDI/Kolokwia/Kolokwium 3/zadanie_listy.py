#rozdzielenie do 2 list, gdzie do pierwszej trafiaja te elementy, ktore wystapily 2 razy
#reszta do drugiej

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def occured_2_times(p, val):
    counter = 0
    while p is not None:
        if p.val == val:
            counter += 1
        p = p.next
    return counter == 2

def solve(p):
    a = Node(None)
    b = Node(None)
    head = p
    while p is not None:
        q = p
        if occured_2_times(head, q.val):
            q.next = a.next
            a.next = q
        else:
            q.next = b.next
            b.next = q
        p = p.next

