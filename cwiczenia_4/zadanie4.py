# x nalezy od 0 do 10^9 - 1
# błyskawicznie generowane ciągi, krótki ciąg z dużego zakresu, ile różnych liczb się znajduje w tym ciągu
# w O(1) odpowiedz, odpowiednia struktura danych

def partition(t, lo, hi):
    pivot = (lo + hi) // 2
    i = lo
    j = hi

    while True:
        while t[i] < t[pivot]:
            i += 1
        while t[j] > t[pivot]:
            j -= 1
        if i >= j:
            return j
        t[i], t[j] = t[j], t[i]


def quicksort(t, left, right):
    if left < right:
        q = partition(t, left, right)
        quicksort(t, left, q - 1)
        quicksort(t, q + 1, right)

    return t

t = [4, 1, 7, 10, 3, 2, 1]
t = quicksort(t, 0, len(t) - 1)
print(t)