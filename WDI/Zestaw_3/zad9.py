def subsequence(tab):
    i = 0
    max = 1
    curr_max = 1
    while i < len(tab) - 2:
        curr_max = 1
        while tab[i] - tab[i+1] < 0:
            i += 1
            curr_max += 1
        if curr_max > max:
            max = curr_max
        i += 1
    return max

tab = list(map(int, input().split()))
print(subsequence(tab))