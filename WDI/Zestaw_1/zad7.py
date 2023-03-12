n = int(input())
a, b = 1, 1

while a <= n:
    if a * b == n:
        print('TAK')
        exit()
    temp = a
    a = b
    b = temp + b
    

print('NIE')