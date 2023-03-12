# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek. 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def is_valid(num):
    one_count = 0
    two_count = 0
    
    while num > 0:
        digit = num % 3
        if digit == 1:
            one_count += 1
        if digit == 2:
            two_count += 1
        num //= 3
    return one_count > two_count

def solve(p):
    q = Node(0)
    q.next = p
    while p.next is not None:
        if is_valid(p.val):
            q.next = p.next
        q = p
        p = p.next

