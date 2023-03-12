class Node:
    def __init__(self) -> None:
        self.next = None
        self.down = None

def sf(T, Tw, Tk):
    w_l = len(T)
    k_l = len(T[0])
    for row in range(w_l, -1, -1):
        for col in range(k_l, -1, -1):
            if T[row][col]:
                p = Node()
                p.next = Tw[row]; Tw[row] = p
                p.down = Tk[col]; Tk[col] = p