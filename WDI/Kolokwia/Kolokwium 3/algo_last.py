# Dane są dwa jednokierunkowe łańcuchy odsyłaczowe (listy)
# Każdy łańcuch zawieraj niepowtarzające się liczby naturalne. W pierwszym łańcuchu liczby są
# posortowane rosnąco, a w drugim nie. Proszę napisać funkcję usuwającą z obu łańcuchów liczby
# występujące w obu łańcuchach. Do funkcji należy przekazać wskazania na oba łańcuchy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów. 

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def solve(A, B):
    count = 0
    wartA = Node(0, A)
    wartB = Node(0, B)
    q2 = wartB
    p2 = B
    while p2 is not None:
        q1 = wartA
        p1 = q1.next
        val = p2.val
        while p1 is not None and p1.val < val:
            q1, p1 = p1, p1.next
        #znalazlem taka sama wartosc
        if p1 is not None and p1.val == val:
            q1.next = p1.next
            q2.next = p2.next
            p2 = p2.next
            count += 2
        else:
            q2, p2 = p2, p2.next
       
        


