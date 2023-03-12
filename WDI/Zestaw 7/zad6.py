# Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def add(p, val):
    new_element = Node(val)
    if p is None:
        return new_element
    while p.next is not None:
        p = p.next
    p.next = new_element
    return p

llist = None    
llist = add(llist, 10)
print(llist)
