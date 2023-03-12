# 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, ind, val=0):
        self.val = val
        self.next = None
        self.ind = ind

class SparseArray:
    def __init__(self, size):
        self.p = Node(0)
        self.max_ind = size

    def return_element(self, ind):
        if 0 > ind >= self.max_ind:
            print('Invalid index')
            return
        p = self.p
        while p is not None and p.ind < ind:
            p = p.next
        if p.ind == ind:
            return p.val
        if p is None or p.ind > ind:
            return 0

    def set_value(self, ind, val):
        if 0 > ind >= self.max_ind:
            print('Invalid index')
            return
        p = self.p
        new_element = Node(ind, val)
        q = None
        while p is not None and p.ind < ind:
            q = p
            p = p.next
        if p is None:
            q.next = new_element
            return
        if p.ind == ind:
            p.val = val
        if p.ind > ind:
            q.next = new_element
            new_element.next = p

    def display(self):
        p = self.p
        while p is not None:
            print(f'A[{p.ind}] = {p.val}')
            p = p.next

p = SparseArray(100)
# SparseArray.set_value(arr, 10, 4)
# arr.set_value(10, 4)
# SparseArray.display(arr)

p.set_value(10, 4)
p.set_value(2, 3)
p.set_value(0, 4)
p.set_value(50, 89)
print(p.return_element(13))
print(p.return_element(10))
p.display()
    


    
