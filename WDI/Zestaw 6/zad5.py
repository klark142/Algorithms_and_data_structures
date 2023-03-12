# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. 
# Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, 
# a dla ciągu 110100 nie jest możliwe.
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (n + 2) == 0:
            return False
    return True

def solve(T):
    n = len(T)
    def recur(T, i, currV, currV_len):
        if i == n - 1:
            return is_prime(currV)
        #odcinamy
        a = False
        if is_prime(currV):
            a = recur(T, i + 1, T[i + 1], 1)
        #przedluzanie
        b = recur(T, i + 1, currV * 2 + T[i + 1], currV_len + 1)
        return a or b
    return recur(T, 0, 0, 0)


def solve2(T):
    n = len(T)
    def recur(T, i):
        if i == n:
            return True

        result = False
        val = 0
        for length in range(1, len(T) - i + 1):
            val = val * 2 + T[i + length - 1]
            if is_prime(val):
                result = result or recur(T, i + length)
        return result
    return recur(T, 0)


print(solve2([1, 1, 0, 1, 0, 0]))  # exp False
print(solve2([1, 1, 1, 0, 1, 1]))  # exp True

        


        



