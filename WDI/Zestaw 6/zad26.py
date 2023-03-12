from math import isqrt

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def rek(a, b, x=0):
    if a == 0 and b == 0:
        if not is_prime(x): return 1
        return 0
    if a > 0:
        A = rek(a - 1, b, x + 2 ** (a + b - 1))
    if b > 0:
        B = rek(a, b - 1, x)
    return A + B

def solve(a, b):
    x = 2 ** (a + b - 1)
    return rek(a - 1, b, x)