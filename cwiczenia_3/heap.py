def heapify(arr, idx, n):
    l = 2 * idx + 1
    r = l + 1
    m = idx
    if l < n and arr[l] > arr[m]:
        m = l
    if r < n and arr[r] > arr[m]:
        m = r
    if m != idx:
        arr[m], arr[idx] = arr[idx], arr[m]
        heapify(arr, m, n)


# k list, suma długości to n
# jak scalić te listy najwydajniej

# struktura danych insert min max wszystko w czasie logn (dwa kopce min i max)
# teraz chcemy też usunac min mix -> bst,

# pd: logn insert i usunac mediane