def insert_sort(t):
    n = len(t)
    for i in range(1, n - 1):
        temp = t[i]
        j = i - 1
        while j >= 0 and temp < t[j]:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = temp
    return t


print(insert_sort([7, 4, 10, 1, 3]))