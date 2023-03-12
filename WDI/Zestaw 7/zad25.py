# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.

def solve(p):
    p1 = p.next
    p2 = p.next.next
    while p1 != p2:
        p1 = p.next
        p2 = p.next.next
    
def dlugosc_cyklu(p1):
    p2 = p1
    count = 0
    while True:
        p2 = p2.next
        count += 1
        if p1 == p2:
            break
    return count

#pomnozyc dwie liczby
