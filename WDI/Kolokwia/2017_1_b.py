# def is_valid(num):
#     a1, a2 = 1, 1
#     b1, b2 = 1, 1
#     sum = 0
#     while True:
#         sum += b1
#         b1, b2 = b2, b1 + b2
#         if sum == num:
#             return False
#         if sum > num:
#             while True:
#                 sum -= a1
#                 a1, a2 = a2, a1 + a2
#                 if sum == num:
#                     return False
#                 if sum < num:
#                     return True

def is_valid(num):
    a1, a2 = 1, 1
    b1, b2 = 1, 1
    sum = 0
    while sum < num:
        sum += b1
        b1, b2 = b2, b1 + b2
    if sum == num:
        return True

    while sum > num:
        sum -= a1
        a1, a2 = a2, a1 + a2
    if sum == num:
        return True
    
    return False

def solve(n):
    while True:
        n += 1
        if not is_valid(n):
            return n

print(solve(15))
