def move(T):
    n = len(T)
    rows = [False for _ in range(n)]
    cols = [False for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if T[row][col] == True:
                rows[row] += 1
                cols[col] += 1
    
    #w jednym wierszu nie ma wiezy
    row_sup = None
    row_inf = None
    for i in range(n):
        if rows[i] >= 2:
            row_sup = i
        if rows[i] == 0:
            if row_inf is not None:
                break
            row_inf = i
    
    if row_sup is not None and row_inf is not None:
        for col in range(n):
            if T[row_sup][col] == True:
                col_from = col
        return (row_sup, col_from), (row_inf, 0)
    
    #w jednej kolumnie nie ma wiezy
    col_sup = None 
    col_inf = None
    for i in range(n):
        if cols[i] >= 2:
            col_sup = i
        if cols[i] == 0:
            col_inf = i
    
    for row in range(n):
        if T[row][col_sup] == True:
            row_from = row
    return (row_from, col_sup), (0, col_inf)


