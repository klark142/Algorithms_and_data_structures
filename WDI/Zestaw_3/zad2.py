#a, b = map(int, input().split())
#print(sorted(str(a)) == sorted(str(b)))

def digit_count(num):
    result = 0
    while num > 0:
        num //= 10
        result += 1
    return result

def check(a, b):
    digits = [0 for _ in range(10)]
    while a > 0:
        last_digit_a = a % 10
        digits[last_digit_a] += 1
        a //= 10
    while b > 0:
        last_digit_b = b % 10
        digits[last_digit_b] -= 1
        b //= 10
    for i in range(10):
        if digits[i] != 0:
            return False
    return True



a, b = map(int, input().split())
print(check(a, b))


