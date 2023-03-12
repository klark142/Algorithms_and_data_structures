def subsequence(tab):
    i = 0
    max = 1
    while i < len(tab) - 2:    
        q = tab[i+1] / tab[i]
        curr_max = 1
        while tab[i+1] / tab[i] == q:
            i += 1
            curr_max += 1
        i += 1
        if curr_max > max:
            max = curr_max
    return max 

tab = list(map(int, input().split()))
print(subsequence(tab))
            
        