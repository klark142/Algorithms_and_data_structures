from math import isqrt
#not working
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(6, isqrt(num) + 1, 6):
        print(i)
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
    return True

print(is_prime(25))



t2 = [
    [1,2,5,4,5],
    [1,10,2,9,34],
    [2,4,1,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]

