# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. 
# Dana jest tablica T[N] zawierająca liczby naturalne. 
# Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

def weight(num):
    factor = 2
    res = 0
    while num != 1:    
        if num % factor == 0:
            res += 1
        while num % factor == 0:
            num //= factor
        factor += 1
    return res

def recur(w, i=0, sum1=0, sum2=0, sum3=0):
    if i == len(w):
        return sum1 == sum2 == sum3
    return recur(w, i + 1, sum1 + w[i], sum2, sum3) or \
        recur(w, i + 1, sum1, sum2 + w[i], sum3) or \
        recur(w, i + 1, sum1, sum2, sum3 + w[i])


def solve(T):
    w = [weight(t) for t in T]
    return recur(w)

print(solve([1, 2, 3, 10, 11, 13]))


