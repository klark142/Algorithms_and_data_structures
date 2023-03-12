# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def solve(p, val):
    head = p
    if p is None:
        return Node(val)
    while p is not None and p.val != val:
        q = p
        p = p.next
    if p is None:
        q.next = Node(val)
    elif p.val == val:
        q.next = p.next
    return head
    

    