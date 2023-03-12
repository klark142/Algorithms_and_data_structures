import math

def length(num):
    len = 0
    while num > 0:
        len += 1
        num //= 10
    return len

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True 
    if num % 2 == 0 or num % 3 == 0:
        return False 
    for i in range(6, math.isqrt(num) + 1, 6):
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
    return True


def decimal_to_base(num, base, length):
    num_base = [0 for _ in range(length)]
    for i in range(len(num_base) - 1, -1, -1):
        num_base[i] = num % base 
        num = num // base
    return num_base

def check(t1, t2):
    counter = 0
    for i in range(0, 3 ** len(t1)):
        s = 0
        mask = decimal_to_base(i, 3, len(t1))
        if mask[i] == 0:
            s += t1[i]
        if mask[i] == 1:
            s += t2[i]
        if mask[i] == 2:
            s += t1[i]
            s += t2[i]
        if is_prime(s):
            counter += 1

t1 = [1,4,52,3,5,2,35]
t2 = [33,0,93,5,12,2,5]
print(check(t1, t2))




    
