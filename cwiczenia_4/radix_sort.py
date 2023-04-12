from random import randint


def counting_sort(arr, place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        count_index = (arr[i] // place) % 10
        count[count_index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    # place elements in sorted order
    i = n - 1
    while i >= 0:
        count_index = (arr[i] // place) % 10
        output[count[count_index] - 1] = arr[i]
        count[count_index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(arr)

    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10


t = [randint(1, 1000) for _ in range(10)]
radix_sort(t)
print(t)