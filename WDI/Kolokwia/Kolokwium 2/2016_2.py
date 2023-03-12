def zlicz_jedynki(n):
    res = 0
    while n > 0:
        if n % 2 == 1:
            res += 1
        n //= 2
    return res

t = [2, 3, 5, 7, 11, 13, 16]
t2 = [zlicz_jedynki(n) for n in t]

def solve(t):
    n = len(t)
    t2 = [zlicz_jedynki(n) for n in t]
    def recur(t2, s1=0, s2=0, s3=0, i=0):
        if i == n and s1 == s2 == s3:
            return True
        if i == n and (s1 != s2 or s2 != s3):
            return False
        
        return recur(t2, s1 + t2[i], s2, s3, i + 1) or \
            recur(t2, s1, s2 + t2[i], s3, i + 1) or \
            recur(t2, s1, s2, s3 + t2[i], i + 1)
    
    