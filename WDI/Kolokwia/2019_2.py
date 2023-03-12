def is_valid(num):
    count = 0
    while num > 0:
        digit = num % 2
        num //= 2
        if digit == 1:
            count += 1
    if count % 2 == 0:
        return 1
    else: return 0

def solve(t):
    n = len(t)
    for i in range(n):
        for j in range(n):
            t[i][j] = is_valid(t[i][j])
    for w in range(n):
        for k1 in range(n):
            for k2 in range(n):
                if k1 == k2:
                    continue
                t2 = [[t[x][y] for x in range(n)] for y in range(n)]
                for i in range(n):
                    t2[w][i] = 1
                    t2[i][k1] = 1
                    t2[i][k2] = 1
                if suma(t2) == 3 * n - 2:
                    return True
    return False

def suma(t):
    n = len(t)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += t[i][j]
    return sum
    
                
            


t2 = [
    [1,2,5,4,5],
    [1,10,2,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,4,16,1]
]