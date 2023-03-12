def nwd(a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a

def nww(a, b):
    return a * b / nwd(a, b)

n1, n2, n3 = map(int, input().split())
print(int((nww(nww(n1, n2), n3))))
