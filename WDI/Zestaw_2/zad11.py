def incr_number(num):
    last = num % 10
    num = num // 10

    while num > 0:
        if last <= num % 10:
            return False
        last = num % 10
        num = num // 10
    return True



num = int(input())
print(incr_number(num))
