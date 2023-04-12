from random import randint


def merge_sort(t):
    if len(t) > 1:
        mid = len(t) // 2
        left = t[:mid]
        right = t[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                t[k] = left[i]
                i += 1
            else:
                t[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            t[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            t[k] = right[j]
            j += 1
            k += 1

    return t


t = [randint(1, 50) for _ in range(20)]
print(t)
print(merge_sort(t))