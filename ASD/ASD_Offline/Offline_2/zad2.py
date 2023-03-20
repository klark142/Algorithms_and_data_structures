from zad2testy import runtests
# Jakub Karoń
# Algorytm wykorzystuje zauważoną własność zadania, polęgającą na tym, że nie ma znaczenia w jakiej
# kolejności będziemy zbierać obszary ze śniegiem, ponieważ od każdej z tych wartości odejmujemy z czasem taką samą
# liczbę. Wnioskujemy zatem, że dążymy jedynie do zebrania jak największych wartości. Złożoność obliczeniową
# algorytmu można opisać jako O(nlogn), ze względu na to, że na początku musimy posortować tablicę, a następnie
# maksymalnie przejdziemy po tablicy jeden raz, zatem O(nlong + n) = O(nlogn). Jako algorytm sortujący wykorzystałem
# sortowanie przez kopcowanie.


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(arr, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and arr[l] > arr[max_ind]:
        max_ind = l
    if r < n and arr[r] > arr[max_ind]:
        max_ind = r

    if max_ind != i:
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
        heapify(arr, max_ind, n)


def heap_sort(arr):
    n = len(arr)
    # build heap
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, i, n)

    day = 0
    for i in range(n - 1, -1, -1):
        # sprawdzenie, czy opłaca się uwzględniać dane pole w sortowaniu
        if arr[0] - day > 0:
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, 0, i)
        day += 1

    return arr


def reverse_array(arr):
    end = len(arr) - 1
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def snow( S ):
    # tu prosze wpisac wlasna implementacje
    heap_sort(S)
    reverse_array(S)
    idx = -1
    result = 0
    current_val = 0
    while current_val >= 0:
        result += current_val
        idx += 1
        current_val = S[idx] - idx

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
