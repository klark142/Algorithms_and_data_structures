from zad1testy import runtests


def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, key)
        merge_sort(right, key)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
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


def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    aux_arr = []
    for i in range(n):
        aux_arr.append([T[i], i])

    merge_sort(aux_arr, 0)

    max_diff = 0
    for i in range(n):
        max_diff = max(max_diff, abs(aux_arr[i][1] - i))

    return max_diff

runtests( chaos_index )
