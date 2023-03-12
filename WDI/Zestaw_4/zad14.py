def is_valid(a, b):
    bin_a = [0 for _ in range(64)]
    bin_b = [0 for _ in range(64)]
    i_a = 0
    i_b = 0
    while a > 0:
        bin_a[i_a] = a % 2
        a //= 10
        i_a += 1
    while b > 0:
        bin_b[i_b] = b % 2
        b //= 10
        i_b += 1
    count_a = 0
    count_b = 0
    for i in range(64):
        if bin_a[i] == 1:
            count_a += 1
        if bin_b[i] == 1:
            count_b += 1
    return count_a == count_b
    

print(is_valid(22, 14))