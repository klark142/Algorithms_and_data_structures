from random import randint

def calc_sum(t2):
    row_sum = [0 for _ in range(len(t2))]
    col_sum = [0 for _ in range(len(t2))]
    #column sum
    for col in range(len(t2)):
        for row in range(len(t2)):
            col_sum[col] += t2[row][col]
            row_sum[col] += t2[col][row]     
    return col_sum, row_sum
      
def highest_quotient(t2):
    col_sum, row_sum = calc_sum(t2)
    curr_highest = 0
    highest = 0
    for i in range(len(t2)):
        for j in range(len(t2)):
            curr_highest = col_sum[j] / row_sum[i]
            if curr_highest > highest:
                highest = curr_highest
                max_i, max_j = i, j
    return max_i, max_j, highest



def solve(t2):
    max_row_sum = 0
    max_row = None
    for row in range(len(t2)):
        sum=0
        for col in range(len(t2)):
            sum += t2[row][col]
        if max_row is None or sum > max_row_sum:
            max_row_sum = sum
            max_row = row
    
    min_col_sum = 0
    min_col = None
    for col in range(len(t2)):
        sum=0
        for row in range(len(t2)):
            sum += t2[row][col]
        if min_col is None or sum < min_col_sum:
            min_col_sum = sum
            min_col = col
    
    return max_row, min_col, max_row_sum / min_col_sum

#                       max_p   min_p   max_n   min_n
    # max_positive_row  -       +       -       -
    # min_positive_row  -       -       -       -
    # max_negative_row  -       -       -       +
    # min_negative_row  -       -       -       -
    
    


#n = int(input('Liczba wierszy i kolumn: '))
#t2 = [[randint(1, 100) for _ in range(n)] for _ in range(n)]

t2 = [
    [2,2,22,44,44],
    [1,1,1,9,39],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]
print(highest_quotient(t2))