# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def delete_even(p):
    i = p
    while i is not None and i.next is not None:
        i.next = i.next.next
        i = i.next
    return p
        