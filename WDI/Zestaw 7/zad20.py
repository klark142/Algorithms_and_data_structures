# Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
# napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
# powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]

class Node:
    def __init__(self, val):
        self.next = None
        self.val = (0,0)

def merge(first):
    p = first 
    while p is not None:
        l = p
        q = p.next
        while q is not None:
            new = scal(p.val, q.val)
            if new:
                p.val = new
                l.next = q.next
            else:
                l = q
            q = q.next
            p = p.next

def scal(k1, k2):
    if k1[1] >= k2[0] and k2[1] >= k1[0]:
        return(min(k1[0], k2[0]), max(k1[1], k2[1]))
    return None


