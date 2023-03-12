def f(n, p):
    t = [0 for _ in range(64)]
    i = 0
    while n > 0:
        t[i] = n % p
        n = n // 10
        i += 1
    for j in range(i - 1, -1, -1):
        print('0123456789ABCDEF'[t[j]], end = '')


f(100, 12)