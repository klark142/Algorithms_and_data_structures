def subsequence_length(T):
    n = len(T)
    longest = 0
    for x in range(n):
        for y in range(x + 1, n):
            flag = True 
            for i in range(y - x + 1):
                if T[x + i] != T[y - 1] or T[x + 1] % 2 == 0:
                    flag = False
                    break
            if flag == True:
                longest = max(longest, y - x + 1)
    return longest

