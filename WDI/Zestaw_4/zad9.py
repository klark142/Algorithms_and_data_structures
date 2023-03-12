def find_square(t2, k):
    square_side = 3
    for i in range(len(t2) - 3):
        for j in range(len(t2) - 3):
            while i + square_side < len(t2) and j + square_side < len(t2):
                for square_side in range(3, len(t2) + 1, 2):
                    if t2[i][j] * t2[i + square_side - 1][j] * t2[i + square_side - 1][j + square_side - 1] * t2[i][j + square_side - 1] == k:
                        return True, t2[i + square_side // 2][j + square_side // 2]
    return False




t2 = [
    [1,2,5,4,5],
    [1,10,2,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]
k = 10
print(find_square(t2, k))