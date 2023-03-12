class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

def create_empty():
    return Node(None)

def contains(p, element):
    p = p.next
    while p is not None and p.val < element:
        p = p.next
    return p is not None and p.val == element

def insert(p, element):
    new_element = Node(element)
    q = p
    p = p.next
    while p is not None and p.val < element:
        q = p
        p = p.next
    
    if p is not None and p.val == element:
        print('Element already present')
    else:
        new_element.next = p
        q.next = new_element

def delete(p, element):
    q = p
    p = p.next
    while p is not None and p.val < element:
        q = p
        p = p.next
    
    if p is not None and p.val == element:
        q.next = p.next
    else:
        print('Element not found')

def print_set(p):
    p = p.next
    while p is not None:
        print(p.val, end=' ')
        p = p.next
    print()
    return

p = create_empty()
insert(p, 1)
insert(p, 4)
insert(p, 2)
insert(p, 7)
print_set(p)






