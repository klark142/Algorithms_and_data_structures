# posortowana lista z wartownikiem
# funkcja wstawiajaca węzeł z wartością

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(p, new_element):
    g = new_element
    while p.next is not None and p.next.val < new_element.val:
        p = p.next
    p.next = new_element.next
    new_element.next = p
    return g

def insertion_sort_linked_list(p):
    head = p
    while p.next is not None:
        temp = p.next
        p.next = p.next.next
        temp.next = None
        insert_node(head, temp)

# pd: selection sort na linked liscie



