#Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

def f(T, i , r):
    n = len(T)
    if r == 0:
        return True
    if r < 0 or i > n - 1:
        return False
    
    return f(T, i + 1, r) or f(T, i + 1, r - T[i]) or f(T, i + 1, r + T[i])

T = [1, 2, 4, 10, 14]
print(f(T, 0, 15))