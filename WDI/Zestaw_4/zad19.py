def solve(T, k):
    count = 0
    for row in range(len(T)):
        for col in range(len(T)):
            #up-left
            if row > 0 and col > 1:
                if T[row][col] * T[row - 1][col - 2] == k:
                    count += 1
            #up-right
            if row > 0 and col < len(T) - 2:
                if T[row][col] * T[row - 1][col + 2] == k:
                    count += 1
            #left-up
            if row > 1 and col > 0:
                if T[row][col] * T[row - 2][col - 1] == k:
                    count += 1
            #left-down
            if row < len(T) - 2 and col > 0:
                if T[row][col] * T[row + 2][col - 1] == k:
                    count += 1
            #right-up
            if row > 1 and col < len(T) - 1:
                if T[row][col] * T[row - 2][col + 1] == k:
                    count += 1
            #right-down
            if row < len(T) - 2 and col < len(T) - 1:
                if T[row][col] * T[row + 2][col + 1] == k:
                    count += 1
            #down-left
            if row < len(T) - 1 and col > 1:
                if T[row][col] * T[row + 1][col - 2] == k:
                    count += 1
            #down-right
            if row < len(T) - 1 and col < len(T) - 2:
                if T[row][col] * T[row + 1][col + 2] == k:
                    count += 1
            
    return count


t2 = [
    [1,2,5,4,5],
    [1,10,50,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,4,16,1]
]

print(solve(t2, 4))