# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z 
# liczby pierwotnej co najmniej jednej cyfry.
from math import isqrt

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, isqrt(num) + 1, 6):
        if num % i == 0 or num % i + 2 == 0:
            return False
    return True

def recursion(num, curr_num=0, digit_count=0):
    if num == 0:
        if is_prime(curr_num) and digit_count >= 2:
            print(curr_num)
        return
    last = num % 10
    recursion(num // 10, curr_num, digit_count) #nie biorę lasta
    recursion(num // 10, last * 10 ** digit_count + curr_num, digit_count + 1) #biorę lasta

print(recursion(1734))