#pociecie liczby n na kawalki tak aby kazdy z kawalkow byl liczba pierwsza oraz 
#liczba kawalkow tez pierwsza, zwracamy wartosc logiczna
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, math.isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def divide(n, parts=0):
    if n == 0:
        if is_prime(parts):
            return True
        else:
            return False
    length = int(math.log10(n)) + 1
    
    for cut_length in range(1, length + 1):
        prefix = n // (10 ** length - cut_length)
        new_n = n % (10 ** length - cut_length)
    
        if is_prime(prefix):
            if divide(new_n, parts + 1):
                return True
    return False

