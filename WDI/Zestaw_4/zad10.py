def zero_in_matrix(t2):
    row_count = 0
    col_count = 0
    for i in range(len(t2)):
        if 0 in t2[i]:
            row_count += 1
        for j in range(len(t2)):
            if t2[j][i] == 0:
                col_count += 1
                break
    return row_count >= len(t2) and col_count >= len(t2)
           
 
        
t2 = [
    [1,2,0,4,5],
    [1,1,2,0,34],
    [2,4,0,1,0],
    [3,0,1,27,3],
    [0,1,0,16,1]
]

print(zero_in_matrix(t2))