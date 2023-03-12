def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

def wzlgednie_pierwsze(a , b):
    return nwd(a, b) == 1

def race(T):
    left_speed = left_rook(T, 0, 0)
    right_speed = right_rook(T, len(T) - 1, 0)
    if left_speed > right_speed:
        return 1
    if right_speed < right_speed:
        return 2
    else:
        return 0
    
def left_rook(T, row, col): #jaka najmniejsza liczba ruchow zeby dotrzec do prawego dolnego rogu
    n = len(T)
    if row == n - 1 and col == n - 1:
        return 0

    best_path = float('inf')
    for new_col in range(col + 1, n):
        if wzlgednie_pierwsze(T[row][col], T[row][new_col]):
            best_path = min(best_path, left_rook(T, row, new_col) + 1)
    
    for new_row in range(row + 1, n):
        if wzlgednie_pierwsze(T[row][col], T[new_row, col]):
            best_path = min(best_path, left_rook(T, new_row, col) + 1)
    
    return best_path

def right_rook(T, row, col): #jaka najmniejsza liczba ruchow zeby dotrzec do prawego dolnego rogu
    n = len(T)
    if row == n - 1 and col == 0:
        return 0

    best_path = float('inf')
    for new_col in range(col + 1, n):
        if wzlgednie_pierwsze(T[row][col], T[row][new_col]):
            best_path = min(best_path, left_rook(T, row, new_col) + 1)
    
    for new_row in range(row + 1, n):
        if wzlgednie_pierwsze(T[row][col], T[new_row, col]):
            best_path = min(best_path, left_rook(T, new_row, col) + 1)
    
    return best_path
        

