def podziel(t, s1, s2, n1, n2, i):
    if s1 == s2 and n1 == n2 and not s1:
        return True
    if i == len(t):
        return False
    
    return podziel(t, s1 + t[i], s2, n1 + 1, n2, i + 1) or \
        podziel(t, s1, s2 + t[i], n1, n2 + 1, i + 1) or \
        podziel(t, s1, s2, n1, n2, i + 1)