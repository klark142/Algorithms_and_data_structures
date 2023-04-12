from zad3testy import runtests
# Jakub Karoń
# Zaproponowany algorytm początkowo sortuje tablicę za pomocą merge sorta, a następnie znajduje
# najczęściej powtarzający się wyraz, który nie jest palindromem oraz taki, który palindromem jest. Jeśli w tablicy
# nie ma długich palindromów, to znaleziony najczęściej powtarzający się wyraz, po uwazględnieniu jego odwrotności,
# na pewno jest wyrazem najcięższym. Może się natomiast zdarzyć, że najczęściej występującym wyrazem był palindrom i
# wówczas musimy sprawdzić, czy nie istnieje inny wyraz, którego liczność wraz z jego odwrotnością jest większa.
# Złożoność algorytmu O(n^2), ponieważ dla każdego wyrazu stosujemy porównania, których złożonością jest O(n)


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
            else:
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


def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    for i in range(n):
        word = T[i]
        if word != word[::-1]:
            T.append(word[::-1])
    n = len(T)
    T = merge_sort(T)
    most_frequent = float("-inf")
    ind = 0
    while ind < n - 1:
        current_most_frequent = 1
        while ind < n - 1 and T[ind] == T[ind + 1]:
            current_most_frequent += 1
            ind += 1
        most_frequent = max(most_frequent, current_most_frequent)
        ind += 1

    return most_frequent


runtests( strong_string, all_tests=True )
