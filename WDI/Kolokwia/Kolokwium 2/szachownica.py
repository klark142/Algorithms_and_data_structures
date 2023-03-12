#tablica 2d, true jesli stoi jakas figura, false jesli nie stoi zadna
#czy istnieje droga skoczka z wiersza 0 do wiersza n-1
#skoczek ma sie poruszac po polach pustych i przyblizac sie do wiersza n-1
#funkcja ma zwrocic najmniejsza mozliwa liczbe ruchow

def contains(row, col, n):
    return row < n and col < n

def solve(t):
    n = len(t)
    def recur(t, row, col, i=0):
        if row == n - 1:
            return i
        
        best_path = float('inf')
        jumps = ((1, 2), (1, -2), (2, 1), (2, -1))
        for jump in jumps:
            new_row = row + jump[0]
            new_col = col + jump[1]
            if contains(new_row, new_col, n) and t[new_row][new_col] == False:
                best_path = min(best_path, recur(t, new_row, new_col, i + 1))
        
        return best_path

        