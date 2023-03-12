# Dana jest tablica T[N] zawierająca liczby naturalne. 
# Po tablicy możemy przemieszczać się według następującej zasady: 
# z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, 
# która zwraca informację czy jest możliwe przejście z pola o indeksie 0 
# na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
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


def solve(t):
    n = len(t)
    t2 = [False for _ in range(n)]
    def recur(t, i=0, cnt=0):
        nonlocal t2
        if i == n:
            return cnt

def solve(t):
    n = len(t)
    def recur(t, i=0, cnt=0):
        if i == n - 1:
            return cnt
        if i > n - 1:
            return -1
        
        for num in range(2, t[i]):
            if t[i] % num == 0 and is_prime(num):
                recur(t, i + num, cnt + 1)
        return -1

print(solve([4, 1, 4, 1, 6, 1, 1, 1]))
