# Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów. 

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def solve(p, a, b):
    count = 0
    p = Node(None, p)
    while p.next is not None:
        if p.next.val % 2 == 0 and p.next.val > 0:
           pass
