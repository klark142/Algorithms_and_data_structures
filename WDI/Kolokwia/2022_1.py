def dwa_czynniki(num):
    count = 0
    factor = 2
    while num != 1:
        if num % factor == 0:
            count += 1
        while num % factor == 0:
            num /= factor
        factor += 1
    return count == 2

def square(T):
    min_tab_side = float('inf')
    length = len(T)
    for row in range(length - 1):
        for col in range(length - 1):
            side = 1
            while row + side < length and col + side < length:
                number = T[row][col] * T[row][col + side] * T[row + side][col + side] * T[row + side][col]
                if dwa_czynniki(number):
                    if side < min_tab_side:
                        min_tab_side = side
                side += 1
    if min_tab_side == ('inf'):
        return 0
    return min_tab_side

T = [
    [1,2,5,4,5],
    [1,10,50,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,4,16,1]
]

print(square(T))

number = 15647
print(list(map(int, str(number))))