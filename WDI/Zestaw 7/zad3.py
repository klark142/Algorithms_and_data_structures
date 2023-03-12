# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

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

def merge_lists(headA, headB):
    first = Node(0)
    tail = first

    while True:
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
        
        if headA.val <= headB.val:
            tail.next = headA
            headA = headA.next
        
        else:
            tail.next = headB
            headB = headB.next
        
        tail = tail.next
    
    return first.next

def scal(p1, p2):
    if p1 == None:
        return p2
    
    if p2 == None:
        return p1
    
    if p1:
        pass

def merge_lists_rek(head1, head2):
    res = None

    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    if head1.val <= head2.val:

        res = head1
        res.next = merge_lists_rek(head1.next, head2)
    
    else:
        res = head2
        res.next = merge_lists_rek(head1, head2.next)
    
    return res

def merge_rek(p1 ,p2):
    if p1 == None:
        return p2
    if p2 == None:
        return p1
    
    if p1.val <= p2.val:
        head = p1
        head.next = merge_rek(p1.next, p2)
    else:
        head = p2
        head.next = merge_rek(p1, p2.next)
    
    
    return head


listA = LinkedList()
listB = LinkedList()
listC = LinkedList()
listA.add_element(2)        
listA.add_element(3)        
listA.add_element(7)
listB.add_element(1)
listB.add_element(6)
listB.add_element(11)
listC.head = merge_lists(listA.head, listB.head)
listC.print_list()


