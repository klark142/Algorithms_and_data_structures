import random

def probability(N):
    t = [0 for _ in range(367)]
    m = 100
    suma_prawd = 0
    for proba in range(m):
        counter = 0
        for osoba in range(N):
            t[random.randint(1, 366)] += 1
        for wynik in t:
            if wynik >= 2:
                counter += 1
        suma_prawd += counter / N
        t = [0 for _ in range(367)]
    return suma_prawd / m
            

print(probability(100))
