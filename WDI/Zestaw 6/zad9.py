#Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

def f(T, r, i = 0, res = []):
    n = len(T)
    if r == 0:
        return True
    if i > n - 1 or r < 0:
        return False
    
    return f(T, r - T[i], i + 1, res + [T[i]]) or f(T, r + T[i], i + 1, res + [- T[i]]) or f(T, r, i + 1, res)

