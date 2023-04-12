import math
import random

# def quicksort(t, l, r):
#     while l < r:
#         q = partition(t, l, r)
#         if q - l > r - q:
#             quicksort(t, q + 1, r)
#             r = q - 1
#         else:
#             quicksort(t, l, q - 1)
#             l = q + 1
#     return t


def quicksort(arr, left, right):
    while left < right:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        left = q + 1

    return arr


# hoare's partition algorithm
def partition(A, lo, hi):
    pivot = A[(lo + hi) // 2]
    # left index
    i = lo
    # right index
    j = hi

    while True:
        while A[i] <= pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


#
# def partition(t, l, r):
#     if l >= r:
#         i = l - 1
#         x = t[r]
#         for j in range(l, r):
#             if t[j] <= x:
#                 i += 1
#                 t[i], t[j] = t[j], t[i]
#         t[i + 1], t[r] = t[r], t[i + 1]
#         return i + 1


t = [16, 9, 94, 7, 85, 75, 30, 74, 68, 69, 16, 16, 16]
print(t)
print(quicksort(t, 0, len(t) - 1))

