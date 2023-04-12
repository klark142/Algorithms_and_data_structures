# find element that would be at ith index in the sorted array
# finding median using quickselect only
from math import floor


def find_median(arr):
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[floor(len(sublist) / 2)] for sublist in sublists]
    if len(medians) <= 5:
        median = sorted(medians)[floor(len(medians) / 2)]
        return median
    else:
        find_median(medians)


print(find_median([1, 2, 3, 4, 5, 6, 7]))

from math import ceil
def quicksort(t, left, right):
    if left < right:
        q = partition(t, left, right)
        quicksort(t, left, q - 1)
        quicksort(t, q + 1, right)


def partition(t, lo, hi):
    pivot = (lo + hi) // 2


def median_of_medians(A, i):
    # divide A into ceil(n/5) arrays containing 5 elements
    n = len(A)
    sublists = [A[j:j+5] for j in range(0, n, 5)]
    medians = [sorted(sublist)[ceil(len(sublist) / 2)] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[ceil(len(medians) / 2)]
    else:
        pivot = median_of_medians(medians, len(medians) / 2)

    # partitioning
