from math import isqrt

def sieve(n):
    tab = [True for _ in range(n)]
    tab[0] = tab[1] = False
    for i in range(2, isqrt(n)):
        if tab[i]:
            for j in range(i ** i, n, i):
                tab[j] = False
    for k in range(n):
        if tab[k]: print(k)



sieve(100)
    





