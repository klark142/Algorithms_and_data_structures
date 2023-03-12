# Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
# sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
# iloczynem dokładnie dwóch liczb pierwszych. Oba kawałki powinny być jednakowej długości.

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

def is_valid(num):
    factor = 2
    counter = 0
    num_copy = num
    while num != 1:
        if is_prime(factor) and num % factor == 0:
            num /= factor
            counter += 1
        factor += 1
        if counter > 2 or factor > num_copy:
            return False
    return True

# def solve(t1, t2):
#     n = len(t1)
#     for length in range(1, n + 1):
#         ind = 0
#         for i in range(length):
#             while ind + length < n + 1:

            

def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr

print(bubble_sort([1, 4, 5, -4, 0, 1]))