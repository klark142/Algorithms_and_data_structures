from zad3testy import runtests


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def SortTab(T,P):
    # tu prosze wpisac wlasna implementacje
    max_interval = 0
    for i, j, k in P:
        max_interval = max(max_interval, j)

    buckets = [[] for _ in range(10)]
    for value in T:
        new_ind = int((value / max_interval) * 10)
        if new_ind != 10:
            buckets[new_ind].append(value)
        else:
            buckets[9].append(value)

    for bucket in buckets:
        insertion_sort(bucket)

    ind = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            T[ind] = buckets[i][j]
            ind += 1

    return T

runtests( SortTab )
