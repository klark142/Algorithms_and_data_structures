def solve(T):
    n = len(T)
    highest = 0
    smallest = float('inf')
    row_max = 0
    row_min = 0
    for row in range(n):
        number = 0
        mult = 1
        for col in range(n - 1, -1, -1):
            number += T[row][col] * mult
            mult *= 2
        if number > highest:
            highest = number
            row_max = row
        if number < smallest:
            smallest = number
            row_min = row
    return abs(row_max - row_min)
            

T = [
    [1,1,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,1,1],
    [0,0,0,0,1]
]

print(solve(T))

