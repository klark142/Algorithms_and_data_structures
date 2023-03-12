import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(6, math.isqrt(num) + 1, 6):
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
    return True

def digit_count(num):
    return int(math.log10(num)) + 1

def first_digits(num, M):
    return num // 10 ** (digit_count(num) - M)

def last_digits(num, N):
    return num % 10 ** N

def diff_digits(num):
    digits = [0 for _ in range(10)]
    while num > 0:
        last = num % 10
        if digits[last] == 1:
            return False
        digits[last] += 1
        num //= 10
    return True

def solve(num):
    curr_biggest = 0
    biggest = 0
    n = digit_count(num)
    for i in range(n):
        for j in range(0, n - i):
            curr_biggest = 0
            cut_number = last_digits(first_digits(num, n - j), n - i) 
            print(cut_number)
            if diff_digits(cut_number) and is_prime(cut_number):
                curr_biggest = cut_number
            if curr_biggest > biggest:
                biggest = curr_biggest
    return biggest

print(solve(1202742516))


