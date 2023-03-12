class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

def create_empty():
    return Node(None)

def contains(p, element):
    while p is not None:
        if p.val == element:
            return True
        p = p.next
    return False

def insert(p, element):
    if contains(p, element):
        print('Element already present')
        return
    new_element = Node(element)
    new_element.next = p.next
    p.next = new_element

def delete(p, element):
    q = p
    p = p.next
    while p is not None:
        if p.val == element:
            q.next = p.next
            return
        q = p
        p = p.next
    print('Element not found')

def print_list(p):
    p = p.next
    while p is not None:
        print(p.val, end=' ')
        p = p.next
    print()

p = create_empty()
insert(p, 10)
insert(p, 2)
insert(p, 3)
print_list(p)






