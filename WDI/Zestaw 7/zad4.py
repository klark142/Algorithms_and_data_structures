# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.val, end=' ')
            p = p.next
    
    def add_element(self, element):
        new_element = Node(element)
        if self.head is None:
            self.head = new_element
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_element


def reverse(p):
    prev = None
    curr = p
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev #new head

linkedlist = LinkedList()
linkedlist.add_element(1)
linkedlist.add_element(4)
linkedlist.add_element(7)
linkedlist.add_element(10)
linkedlist.print_list(reverse())

    
        