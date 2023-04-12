from random import randint

def partiton(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[i], arr[j]

    arr[right], arr[i + 1] = arr[i + 1], arr[right]
    return i + 1


def find_kth_smallest(arr, k):
    def quick_select(left, right):
        pivot = partiton(arr, left, right)
        if pivot == k + 1:
            return arr[pivot]
        elif pivot > k + 1:
            return quick_select(pivot + 1, right)
        else:
            return quick_select(left, pivot - 1)
    return quick_select(0, len(arr) - 1)


def sum_between(arr, start, end):
    min_val = find_kth_smallest(arr, start - 1)
    max_val = find_kth_smallest(arr, end - 1)
    sum = 0

    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            sum += arr[i]

    return sum
