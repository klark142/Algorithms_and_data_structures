def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    T = sorted(T)
    n = len(T)
    most_frequent = float("-inf")
    ind = 0
    while ind < n - 1:
        current_most_frequent = 1
        current_most_frequent_word = T[ind]
        while T[ind + 1] == T[ind]:
            current_most_frequent += 1
            ind += 1
        most_frequent = max(most_frequent, current_most_frequent)
        if most_frequent == current_most_frequent:
            most_frequent_word = current_most_frequent_word
        ind += 1

    reversed_count = 0
    for j in range(n):
        if T[j][::-1] == most_frequent_word:
            reversed_count += 1

    return most_frequent + reversed_count


T = ["pies", "mysz", "kot", 'tugok', "kogut", "tok", "seip", "kot", 'zsym']
print(strong_string(T))
