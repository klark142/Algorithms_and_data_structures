from math import isqrt

def digit_count(num):
    cnt = 0
    while num > 0:
        cnt += 1
        num //= 10
    return cnt

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

cnt = 0

def solve(num1, num2):
    def recur(num1, num2, curr_num=0):
        global cnt
        if num1 == 0 and num2 == 0:
            print(curr_num)
            if is_prime(curr_num):
                cnt += 1
            return
        #biorę z num 1
        if num1 != 0:
            l1 = digit_count(num1)
            new_num1 = num1 - ((num1 // 10 ** (l1 - 1)) * 10 ** (l1 - 1))
            recur(new_num1, num2, curr_num * 10 + int(num1 / 10 ** (l1 - 1)))
        #biorę z num 2
        if num2 != 0:
            l2 = digit_count(num2)
            new_num2 = num2 - ((num2 // 10 ** (l2 - 1)) * 10 ** (l2 - 1))
            recur(num1, new_num2, curr_num * 10 + int(num2 / 10 ** (l2 - 1)))
    recur(num1, num2)

solve(123, 75)
print(cnt)
        
