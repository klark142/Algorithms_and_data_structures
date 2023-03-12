n = int(input())
a0 = 0
a1 = 1
b0 = 2
b1 = 2

while n == a0:
    print(b0)
    b0, b1 = b1, b0 + 2 * a0
    a0, a1 = a1, a1 - b1 * a0
    n = int(input())

