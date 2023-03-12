# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

def contains(p, target):
    while p is not None:
        if p.val == target:
            return True
        p = p.next
    return False

def member_rek(el, zb):
    return zb is not None and (zb.val == el or member_rek(el, zb.next))
    

def insert_old():
    #todo
    pass

def insert(p, element):
    if not contains(p, element):
        new_element = Node(element)
        new_element.next = p
        return new_element
    print('Element already present')

def delete(p, element):
    q = None
    head = p
    while p is not None:
        if p.val == element:
            if p == head:
                head = p.next
            else:
                q.next = p.next
            return head
        q = p
        p = p.next
    print('Error, element not found')
    return head

def print_list(p):
    while p is not None:
        print(p.val, end=' ')
        p = p.next
    print()

p = Node(1)
p = insert(p, 10)
p = insert(p, 3)
p = insert(p, 2)
p = delete(p, 2)
print_list(p)

    





        