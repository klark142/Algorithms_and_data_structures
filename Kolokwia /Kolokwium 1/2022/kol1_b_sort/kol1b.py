from kol1btesty import runtests
MAX_CHAR = 26


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
            elif right[j] < left[i]:
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


def sort_string(word):
    char_count = [0 for _ in range(MAX_CHAR)]
    result = ''
    for i in range(len(word)):
        char_count[ord(word[i]) - ord("a")] += 1

    for i in range(MAX_CHAR):
        result += char_count[i] * (chr(ord("a") + i))

    return result


def f(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    # sortujemy O(n)
    for i in range(n):
        T[i] = sort_string(T[i])

    T = merge_sort(T)
    print(T)
    most_popular = 0
    i = 0
    while i < n - 1:
        current_popular = 1
        while i < n - 1 and T[i] == T[i + 1]:
            current_popular += 1
            i += 1
        most_popular = max(most_popular, current_popular)
        i += 1

    return most_popular


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
