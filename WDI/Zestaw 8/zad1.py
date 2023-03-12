class Node:
    def __init__(self) -> None:
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        #parent nie zawsze

#wypisanie węzłów w drzewie
def wypisz(p):
    if p is not None:
        print(p.val)
        wypisz(p.right)
        wypisz(p.left)

#Funkcja wypisującą zawartość drzewa (iteracyjnie)
def wypisz_iteracyjnie(el):
    stos = []
    stos.append(el)
    while len(stos) != 0:
        curr = stos.pop()
        if curr != None:
            print(curr.val)
            stos.append(curr.left)
            stos.append(curr.right)
    

#ilość węzłów w drzewie
def policz(p):
    if p == None:
        return 0
    return policz(p.left) + policz(p.right) + 1

#liczba liści w drzewie
def policz_liscie(p):
    if p == None:
        return 0
    if p.left == None and p.right == None:
        return 0
    return policz_liscie(p.left) + policz_liscie(p.right)

#drzewo BST
def contains(p, val):
    if p == None: return False
    if p.val == val: return True
    if val < p.val:
        return contains(p.left, val)
    return contains(p.right, val)

def insert(p, val):
    if p == None:
        p = Node(val)
        return p
    if p.val == val:
        return p
    if val < p.val:
        p.left = insert(p.left, val)
    if val > p.val:
        p.right = insert(p.right, val)
    return p
    
#czy drzewo jest drzewem AVL?
def is_AVL(p):
    if p == None:
        return 0
    left = is_AVL(p.left)
    right = is_AVL(p.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) <= 1:
        return max(left, right) + 1
    return -1

#zadanie 14 - funkcja ackermanna interacyjnie

def f(a, b):
    if a == 0: 
        return b + 1
    if b == 0:
        f(a - 1, 1)
    return f(a - 1, f(a, b - 1))

# def f_iteracyjna(a, b):
#     st.init()
#     st.push(a)
#     st.push(b)
#     while True:
#         b = st.pop()
#         a = st.pop()
#         if a == 0: st.push(b + 1)
#         if b == 0:
#             st.push(a - 1)
#             st.push(1)
#         else:
#             st.push(a - 1)
#             st.push(a)
#             st.push(b - 1)
