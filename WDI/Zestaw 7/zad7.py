# Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def delete_last(p):
    if p is None:
        return p
    if p.next is None:
        return p
    while p.next is not None:
        q = p
        p = p.next
    q.next = None


