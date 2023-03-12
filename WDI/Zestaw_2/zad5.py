def num_length(num):
    length = 0
    while num > 0:
        num = num // 10
        length += 1
    return length

def number_gen(num, i):
    result = 0
    mult = 1
    while num > 0:
        last = num % 10
        num = num // 10
        if i % 2 == 0:
            result += last * mult
            mult *= 10
        i //= 2
    return result

num = int(input())
counter = 0
for i in range(0, 2 ** num_length(num) - 1):
    temp_number = number_gen(num, i)
    if temp_number % 7 == 0:
        print(temp_number)
        counter += 1

print(counter)