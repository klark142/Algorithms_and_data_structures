#working?

def longest_sub(t2):
    curr_longest = 1
    longest = 1
    for i in range(len(t2) - 2):
        for j in range(len(t2) - 2):
            index = 1
            q = t2[i + 1][j + 1] / t2[i][j]
            while q == t2[i + 1][j + 1] / t2[i][j] and i + index < len(t2) and j + index < len(t2):
                curr_longest += 1
                q = t2[i + index][j + index] / t2[i + index - 1][j + index - 1]
                index += 1
            if curr_longest > longest:
                longest = curr_longest
            curr_longest = 0
    return longest

t2 = [
    [1,2,3,4,5],
    [1,3,4,9,34],
    [2,4,9,8,27],
    [3,3,1,26,16],
    [1,1,1,16,80]
]

print(longest_sub(t2))

