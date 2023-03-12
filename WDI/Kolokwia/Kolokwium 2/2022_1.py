def rook(N, L):
    t2 = [[False for _ in range(N)] for _ in range(N)]
    for row, col in L:
        t2[row][col] = True
    
    def recur(row=0, col=0):
        if row == N - 1 and col == N - 1:
            return 0
        best_path = float('inf')
        #ruszanie w dol
        new_row = row + 1
        while new_row < N and t2[new_row][col] == False:
            best_path = min(best_path, recur(new_row, col) + 1)
            new_row += 1
        
        #ruszanie w prawo
        new_col = col + 1
        while new_col < N and t2[row][new_col] == False:
            best_path = min(best_path, recur(row, new_col) + 1)
            new_col += 1
        
        return best_path
    
    a = recur()
    if a == float('inf'):
        return None
    return a