def quicksort(t, l, r):
    while l < r:
        q = partition(t, l, r)
        if q - l > r - q:
            quicksort(t, q + 1, r)
            r = q - 1
        else:
            quicksort(t, l, q - 1)
            l = q + 1
    return t


def partition(t, l, r):
    if l >= r:
        i = l - 1
        x = t[r]
        for j in range(l, r):
            if t[j] <= x:
                i += 1
                t[i], t[j] = t[j], t[i]
        t[i + 1], t[r] = t[r], t[i + 1]
        return i + 1


t = [5, 1, 3, 10, 2, 13]
print(quicksort(t, 0, len(t) - 1))

