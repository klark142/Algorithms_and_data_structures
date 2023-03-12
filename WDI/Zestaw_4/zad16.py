#only digits
def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    return False

def only_prime(num):
    while num > 0:
        last = num % 10
        if not is_prime(last):
            return False
        num //= 10
    return True

def check(t2):
    col = 0
    row = 0
    not_prime = 0
    while col < len(t2):
        num = t2[row][col]
        if only_prime(num):
            row += 1
            col = 0
        col += 1
        if col == len(t2):
            return False
        if row == len(t2):
            return True

t2 = [
    [1,2,5,4,5],
    [1,10,2,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,4,16,1]
]

print(check(t2))