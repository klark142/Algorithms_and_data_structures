def solve(t2):
    max_p = 0
    min_p = float('inf')
    max_n = 0
    min_n = float('-inf')


    #column sums
    for col in range(len(t2)):
        sum_col = 0
        for row in range(len(t2)):
            sum_col += t2[row][col]
        if sum_col <= 0:
            if sum_col < max_n:
                max_n = sum_col
                max_n_col = col
            #max_n = min(max_n, sum_col)
        elif sum_col > 0:
            if sum_col > max_p:
                max_p = sum_col
                max_p_col = col
            #max_p = max(max_p, sum_col)
    #row sums
    for row in range(len(t2)):
        sum_row = 0
        for col in range(len(t2)):
            sum_row += t2[row][col]
        if sum_row < 0:
            if abs(sum_row) < abs(min_n):
                min_n = sum_row
                min_n_row = row
            #min_n = min(abs(min_n), abs(sum_row))
        elif sum_row > 0:
            if sum_row < min_p:
                min_p = sum_row
                min_p_row = row
            #min_p = min(min_p, sum_row)
    
    if max_p / min_p > max_n / min_n:
        return min_p_row, max_p_col
    else: 
        return min_n_row, max_n_col

t2 = [
    [2,2,22,44,44],
    [-100,1,1,9,39],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]


print(solve(t2))
