def nwd(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a

n1, n2, n3 = map(int, input().split())

print(nwd(nwd(n1, n2), n3))