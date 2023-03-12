class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

def dziel(p):
    if p is None:
        return p
    Tp = [None for _ in range(10)]
    Tk = [None for _ in range(10)]
    while p is not None:
        i = p.val % 10
        if Tp[i] is None:
            Tp[i] = p
            Tk[i] = p
        else:
            Tk[i].next = p
            Tk[i] = p
        p = p.next
    result = None
    for i in range(9, -1, -1):
        if Tp[i] is not None:
            Tk[i].next = result
            result = Tp[i]
    return result