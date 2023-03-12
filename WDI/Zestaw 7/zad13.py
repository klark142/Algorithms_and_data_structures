# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów. 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def solve(p):
    while p is not None:
        q = p
        p = p.next
        if q.val > p.val:
            q.next = p.next
        