from zad3testy import runtests


def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    T = sorted(T)
    n = len(T)
    most_frequent = float("-inf")
    most_frequent_palindrome = float("-inf")
    ind = 0
    while ind < n - 1:
        current_most_frequent = 1
        current_most_frequent_palin = 1
        current_most_frequent_word = T[ind]

        if T[ind] == T[ind][::-1]:
            while ind < n - 1 and T[ind + 1] == T[ind]:
                current_most_frequent_palin += 1
                ind += 1

            if current_most_frequent_palin > most_frequent_palindrome:
                most_frequent_palindrome = current_most_frequent_palin

        else:
            while ind < n - 1 and T[ind + 1] == T[ind]:
                current_most_frequent += 1
                ind += 1

            if current_most_frequent > most_frequent:
                most_frequent = current_most_frequent
                most_frequent_word = current_most_frequent_word

        ind += 1

    reversed_count = 0
    for j in range(n):
        if T[j][::-1] == most_frequent_word:
            reversed_count += 1

    return max(most_frequent + reversed_count, most_frequent_palindrome)


runtests( strong_string, all_tests=True )
