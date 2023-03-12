import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, math.isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def num_len(num):
    return int(math.log10(num)) + 1

def rotate(num):
    return (num % 10 ** (num_len(num) - 1)) * 10 + num // 10 ** (num_len(num) - 1)

def digit_product(num):
    res = 1
    while num > 0:
        last = num % 10
        res *= last
        num //= 10
    return res

def solve(num):
    for base in range(2, 17):
        for _ in range(num_len(num)):
            num = rotate(num)
            n_copy = num
            product = 1
            while n_copy > 0:
                digit = n_copy % base
                n_copy //= base
                product *= digit
            if is_prime(product):
                return True
    return None


