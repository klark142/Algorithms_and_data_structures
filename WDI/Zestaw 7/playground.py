#playground

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()
    
    def append(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        cnt = 0
        while curr.next is not None:
            cnt += 1
            curr = curr.next
        return cnt
    
    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
            elems.append(curr_node.val)
        print(elems)

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()


    





