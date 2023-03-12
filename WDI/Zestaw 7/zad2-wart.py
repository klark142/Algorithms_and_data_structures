# 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, val=0, ind=-1):
        self.val = val
        self.next = None
        self.ind = ind

def init():
    p = Node()
    max_ind = int(input('Set the size of the sparse array: '))
    return p

def return_value(p, ind):
    global max_ind
    while p is not None and p.ind < ind:
        p = p.next
    #value not found
    if ind < max_ind:
        return 0
    if p is None:
        print('Invalid index value')
        return    
    #value found
    return p.val

def set_value(p, val, ind):
    global max_ind
    if ind >= max_ind:
        print('Invalid index')
        return
    #index already present
    while p is not None and p.ind != ind:
        p = p.next
    if p is not None and p.ind == ind:
        p.val = val
    #index not present
    else:
        new_element = Node(val, ind)
        q = p
        p = p.next
        while p is not None and p.ind < ind:
            q = p
            p = p.next
        if p is None:
            p.next = new_element

        
        



