from random import randint


def find_kth_smallest(arr, k):
    def quick_select(left, right):
        curr_pivot = partition(arr, left, right)
        if curr_pivot == k - 1:
            return arr[curr_pivot]
        elif curr_pivot > k - 1:
            return quick_select(left, curr_pivot - 1)
        else:
            return quick_select(curr_pivot + 1, right)

    return quick_select(0, len(arr) - 1)


def find_kth_largest(arr, k):
    return find_kth_smallest(arr, len(arr) - k)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def section(T, p, q):
    max_val = find_kth_largest(T, p - 1)
    min_val = find_kth_largest(T, q - 1)
    res = []
    for i in range(len(T)):
        if min_val <= T[i] <= max_val:
            res.append(T[i])
    return res


t = [randint(140, 200) for _ in range(10)]
print(sorted(t, reverse=True))
print(section(t, 4, 7))




