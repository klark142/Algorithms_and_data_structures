from random import randint


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def parent(i):
    return (i - 1) // 2


# O(logn)
def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and arr[l] > arr[max_ind]:
        max_ind = l
    if r < n and arr[r] > arr[max_ind]:
        max_ind = r

    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        heapify(arr, max_ind, n)


# O(n)
def build_heap(arr, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, i, n)


# O(nlogn)
def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def insert_element(arr, key):
    arr.append(key)
    n = len(arr)
    build_heap(arr, n)


def extract_max(arr):
    max_value = arr[0]
    arr[0] = arr[len(arr) - 1]
    heapify(arr, 0, len(arr) - 1)
    return max_value


t = [randint(1, 50) for _ in range(20)]
print(t)
build_heap(t, len(t))
print(t)
insert_element(t, 52)
print(t)
print(extract_max(t))
print(t)