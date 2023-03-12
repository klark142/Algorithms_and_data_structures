# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

def solve(T, k):
    n = len(T)
    def recur(T, s1=0, s2=0, n1=0, n2=0, i=0):
        if s1 == s2 and n1 + n2 == k:
            return True
        if i == n:
            return False
        # biorę do pierwszego zbioru
        # recur(T, s1 + T[i], s2, n1 + 1, n2, i + 1)
        # do drugiego
        # recur(T, s1, s2 + T[i], n1, n2 + 1, i + 1)
        # nigdzie
        # recur(T, s1, s2, n1, n2, i + 1)
        

        return recur(T, s1 + T[i], s2, n1 + 1, n2, i + 1) or \
            recur(T, s1, s2 + T[i], n1, n2 + 1, i + 1) or \
            recur(T, s1, s2, n1, n2, i + 1)
        