from math import sqrt

def opt_products(num):
    q = int(sqrt(num))
    p = q
    curr_n = p * q
    while p * q != num:
        if p * q < num:
            p += 1
        if p * q > num:
            q -= 1
        curr_n = p * q
    return p, q

num = int(input())
print(opt_products(num))
