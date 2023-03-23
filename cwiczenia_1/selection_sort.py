def selection_sort(t):
    n = len(t)
    for i in range(n - 1):
        ind = i
        for j in range(i + 1, n):
            if t[j] < t[ind]:
                ind = j
        t[ind], t[i] = t[i], t[ind]