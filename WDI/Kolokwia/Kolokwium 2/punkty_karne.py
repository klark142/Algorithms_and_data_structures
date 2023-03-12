#krol znajduje sie na 0,0 ma dojsc do n-1,n-1 i zebrac jak najmniej punktow karnych
#rusza sie tylko w prawo lub w dol, pole poczatkowe i startowe ma 0 pkt

def solve(T):
    n = len(T)
    def recur(T, row, col):
        if row == 0 and col == 0:
            return 0
        if row < 0 and col < 0:
            return float('inf')
        return min(recur(T, row - 1, col), recur(T, row, col - 1) + T[row][col])