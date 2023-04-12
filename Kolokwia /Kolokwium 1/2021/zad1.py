from zad1testy import runtests


def quicksort(arr, left, right):
    while left < right:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        left = q + 1

    return arr


# hoare's partition algorithm
def partition(A, lo, hi):
    pivot = A[(lo + hi) // 2]
    # left index
    i = lo
    # right index
    j = hi

    while True:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


def median(t):
    n = len(t)
    aux_arr = [0 for _ in range(n ** 2)]
    aux_arr_ind = 0
    for i in range(n):
        for j in range(n):
            aux_arr[aux_arr_ind] = t[i][j]
            aux_arr_ind += 1

    # aux_arr = quicksort(aux_arr, 0, (n ** 2) - 1)
    aux_arr.sort()
    median_ind = (n ** 2) // 2
    diagonal_nums = 0
    # insert diagonal nums
    if n % 2 == 0:
        row_col = 2
        k = 1
        t[0][0] = aux_arr[median_ind]
        diagonal_nums += 1
        t[1][1] = aux_arr[median_ind - 1]
        diagonal_nums += 1
        while diagonal_nums != n:
            t[row_col][row_col] = aux_arr[median_ind + k]
            t[row_col + 1][row_col + 1] = aux_arr[median_ind - 1 - k]
            diagonal_nums += 2
            row_col += 1
            k += 1
    else:
        t[0][0] = aux_arr[median_ind]
        k = 1
        row_col = 1
        diagonal_nums = 1
        while diagonal_nums != n:
            t[row_col][row_col] = aux_arr[median_ind + k]
            t[row_col + 1][row_col + 1] = aux_arr[median_ind - k]
            diagonal_nums += 2
            k += 1
            row_col += 1

    # insert less or equal
    col_end = 1
    ind = 0
    for row in range(1, n):
        for col in range(0, col_end):
            t[row][col] = aux_arr[ind]

        col_end += 1
        ind += 1

    # insert greater or equal
    ind = n ** 2 - 1
    col_start = 1
    for row in range(0, n - 1):
        for col in range(col_start, n):
            t[row][col] = aux_arr[ind]

        col_start += 1
        ind -= 1

    return t


runtests( median )
