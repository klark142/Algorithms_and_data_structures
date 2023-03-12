def kadane(t):
    curr_max = global_max = t[0]
    for i in range(1, len(t)):
        curr_max = max(t[i], t[i] + curr_max)
        if curr_max > global_max:
            global_max = curr_max
    return global_max


def solve(t2):
    max_row = 0
    max_col = 0
    curr_max_row = 0
    curr_max_col = 0
    for row in range(len(t2)):
        curr_max_row = kadane(t2[row])
        if curr_max_row > max_row:
            max_row = curr_max_row
    for col in range(len(t2)):    
        #col max subarray sum
        curr_max_col = t2[0][col]
        for i in range(1, len(t2)):
            curr_max_col = max(t2[i][col], t2[i][col] + curr_max_col)
            if curr_max_col > max_col:
                max_col = curr_max_col
                print(max_col)
    return max_row, max_col
            




t2 = [
    [3,2,-5,500,-10],
    [1,10,2,9,-4],
    [2,-3,1,1,27],
    [3,3,1,-1,-6],
    [1,1,-7,16,4]
]

print(solve(t2))