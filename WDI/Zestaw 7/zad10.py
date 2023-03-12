# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def add(a, b):
    def rek(p1, p2):
        if p1.next is None:
            value = (p1.val + p2.val) % 10
            h = Node(value)
            return h
        else:
            g = Node()
            con = rek(p1.next, p2.next)
            g.next = con
            g.val = p1.val + p2.val
            if con.val < p1.next.val and con.val < p2.next.val:
                g.val += 1
            g.val %= 10
            return g
