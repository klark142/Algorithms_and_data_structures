def highest_sum(t2):
    highest = 0
    for i in range(len(t2)):
        for j in range(len(t2)):
            sum = 0
            # w lewo
            if j != 0:
                sum += t2[i][j - 1]
            # w prawo
            if j != len(t2) - 1:
                sum += t2[i][j + 1]
            # w dół 
            if i != len(t2) - 1:
                sum += t2[i + 1][j]
            # w górę
            if i != 0:
                sum += t2[i - 1][j]
            if sum > highest:
                highest = sum 
                max_i, max_j = i, j
    return max_i, max_j

t2 = [
    [1,2,5,4,5],
    [1,10,50,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,4,16,1]
]

print(highest_sum(t2))