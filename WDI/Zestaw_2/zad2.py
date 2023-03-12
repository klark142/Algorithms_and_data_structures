a = int(input())
b = int(input())
n = int(input())

if a % b == 0:
    print(a / b)
    exit()
if a % b != 0:
    print(a // b, '.', end = '')

a = a % b
while a > 0 and n > 0:
    a = a * 10
    print (a // b, end = '')
    a = a % b
    n -= 1

