import random

def odd_digit_check(t):
    count = 0
    for number in t:
        while number > 0:
            last_digit = number % 10
            if last_digit % 2 == 1:
                count += 1
                break
            number //= 10
    if count != n:
        return False
    else: return True 


n = int(input())
t = [random.randint(1, 1000) for _ in range(n)]
print(odd_digit_check(t))
