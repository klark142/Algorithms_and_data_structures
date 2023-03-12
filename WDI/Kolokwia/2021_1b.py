#Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci indeks
#największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
#mniejszych od niej lub None, jeżeli taka liczba nie istnieje.

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

def solve(t):
    biggest = 0
    for i in range(len(t)):
        product = 1
        max_ind = t[i] - 1
        while max_ind > 0:
            if is_prime(t[max_ind]):
                product *= t[max_ind]
            max_ind -= 1
        if product == t[i] and t[i] > biggest:
            biggest = t[i]
            biggest_ind = i
    if biggest_ind == 0:
        return None
    else: return biggest_ind

print(solve([1, 3, 1, 3, 4, 2, 6]))