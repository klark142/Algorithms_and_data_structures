from random import randint


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def is_two_sum(arr, n, index):
    i = 0 if index != 0 else 1
    j = n - 1 if index != n - 1 else n - 2
    target = arr[index]
    while i < j:
        if i != index and j != index:
            current_sum = arr[i] + arr[j]
        if current_sum < target:
            i += 1
        elif current_sum > target:
            j -= 1
        else:
            return True

    return False


def solve(arr):
    n = len(arr)
    merge_sort(arr)
    for i in range(n):
        if not is_two_sum(arr, n, i):
            return False
    return True


t = [randint(-20, 20) for _ in range(20)]
print(solve(t))
print(sorted(t))