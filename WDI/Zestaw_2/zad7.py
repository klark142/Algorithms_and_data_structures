def is_multiple(num):
    n = 1
    a = 0
    while a <= num:
        a = n * n + n + 1
        if num % a == 0:
            return True
        n += 1
    return False

num = int(input())
print(is_multiple(num))