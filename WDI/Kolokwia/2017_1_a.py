def is_valid(a, b):
    digits = [0 for _ in range(10)]
    while a > 0:
        last = a % 10
        digits[last] += 1
        a //= 10
    while b > 0:
        last = b % 10
        if digits[last] > 0:
            return False
        b //= 10
    return True

def solve(a, b):
    for base in range(2, 17): 
        a_base = 0
        b_base = 0
        mult_a = 1
        mult_b = 1
        a_copy = a
        b_copy = b
        #convert a
        while a_copy > 0:
            digit = a_copy % base
            a_base += digit * mult_a
            a_copy //= base
            mult_a *= 10
        #convert b
        while b_copy > 0:
            digit = b_copy % base
            b_base += digit * mult_b
            b_copy //= base
            mult_b *= 10
        print(a_base, b_base)
        if is_valid(a_base, b_base):
            return base
    return False

print(solve(123, 522))