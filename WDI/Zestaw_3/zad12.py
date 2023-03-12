import random

def subsequence(tab):
    i = 0
    max_pos = 1
    max_neg = 1
    while i < len(tab) - 2:    
        r = tab[i+1] - tab[i]
        if r > 0:
            curr_max_pos = 1
            while tab[i+1] - tab[i] == r:
                i += 1
                curr_max_pos += 1
            i += 1
            if curr_max_pos > max_pos:
                max_pos = curr_max_pos
        elif r < 0:
            curr_max_neg = 1
            while tab[i+1] - tab[i] == r:
                i += 1
                curr_max_neg += 1
            i += 1
            if curr_max_neg > max_neg:
                max_neg = curr_max_neg
    return max_pos, max_neg


n = int(input('Rozmiar tablicy: '))
tab = [random.randint(1, 99) for _ in range(n)]
print(abs(subsequence(tab)[0] - subsequence(tab)[1]))