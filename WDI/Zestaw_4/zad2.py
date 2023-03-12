def only_even(num):
    while num > 0:
        even, odd = 0, 0
        last = num % 10
        if last % 2 == 1:
            return False
        num //= 10
    return True

def only_odd(num):
    while num > 0:
        last = num % 10
        if last % 2 == 0:
            return False
        num //= 10
    return True

def check(t2):
    row = 0
    col = 0
    even_counter = 0
    for _ in range(len(t2)):
        while col < len(t2):
            if only_even(t2[row][col]):
                even_counter += 1
            if even_counter == len(t2):
                return False
            col += 1
        even_counter = 0
        col = 0
        row += 1
    return True

def solve(t2):
    row = 0 
    col = 0
    while col < len(t2):
        if only_odd(t2[row][col]):
            row += 1
            col = 0
        else:
            col += 1
        if col == len(t2):
            return False
        if row == len(t2):
            return True

t2 = [
    [2,2,22,44,55],
    [1,1,2,9,34],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]

print(check(t2)) 
print(solve(t2))