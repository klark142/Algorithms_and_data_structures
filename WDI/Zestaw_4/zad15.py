from math import isqrt 

#only digits
def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    return False

def prime_digit_check(num):
    while num > 0:
        last = num % 10
        if is_prime(last):
            return True
        num //= 10
    return False

def solve(t2):
    col = 0
    row = 0
    while col < len(t2):
        if prime_digit_check(t2[row][col]):
            col += 1
        else: 
            row += 1
            col = 0
        if col == len(t2):
            return True
        if row == len(t2):
            return False
    

t2 = [
    [3,2,5,42,5],
    [1,10,2,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]

print(solve(t2))