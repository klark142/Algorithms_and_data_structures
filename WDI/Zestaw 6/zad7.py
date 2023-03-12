# Dany jest zestaw odważników T[N]. Napisać funkcję, 
# która sprawdza czy jest możliwe odważenie określonej masy. 
# Odważniki można umieszczać tylko na jednej szalce.

def f(T, i, r):
    n = len(T)
    if r == 0:
        return True
    if r < 0 or i > n - 1:
        return False
    
    return f(T, i + 1, r) or f(T, i + 1, r - T[i])
    #          nie biorę        biorę