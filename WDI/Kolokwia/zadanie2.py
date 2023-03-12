# Zad. 2. Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
# można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy był wielokrotnością
# (co najmniej dwukrotnością) kwadratu dowolnej liczby naturalne większej od 1.

import math
# def is_valid(num):
#     multiple = 2
#     podstawa = 2
#     while podstawa < num:
#         a = multiple * podstawa ** 2
#         while a <= num:
#             a = multiple * podstawa ** 2
#             if num == a:
#                 return True
#             multiple += 1
#         podstawa += 1
#     return False

def is_valid(num):
    for podstawa in range(2, num):
        for wielokrotnosc in range(2, num):
            x = wielokrotnosc * podstawa ** 2
            if x == num:
                return 0
    return 1

def suma(t):
    n = len(t)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += t[i][j]
    return sum

def solve(t):
    n = len(t)
    for i in range(n):
        for j in range(n):
            t[i][j] = is_valid(t[i][j])
    for w in range(n):
        for k1 in range(n):
            for k2 in range(n):
                if k1 == k2:
                    continue
                t2 = [[t[x][y] for x in range(n)] for y in range(n)]
                for i in range(n):
                    t2[w][i] = 1
                    t2[k1][i] = 1
                    t2[k2][i] = 1
                if suma(t2) == 3 * n - 2:
                    return True
    return False


