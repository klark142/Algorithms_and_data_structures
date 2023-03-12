def digit_number(num):
    digit = 0
    while num > 0:
        num = num // 10
        digit += 1
    return digit

def check(num):
    digit_num = digit_number(num)
    while num > 0:
        last = num % 10
        if last == digit_num:
            return True
        num = num // 10
    return False

num = int(input())
print(check(num))
    
