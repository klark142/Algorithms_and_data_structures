def is_unique(num):
    candidate = num % 10
    while num > 0:
        num = num // 10
        last = num % 10
        if last == candidate:
            return False
    return True

num = int(input())
print(is_unique(num))