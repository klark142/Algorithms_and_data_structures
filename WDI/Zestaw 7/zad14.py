# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich
# elementów. 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def solve(p):
    q = Node(1.2)
    q.next = p
    while p.next is not None:
        if p.next.val % p.val == 0:
            q.next = p.next
        q = p
        p = p.next
    
