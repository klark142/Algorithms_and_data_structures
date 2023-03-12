suma = int(input())

fib = []
a = 1
b = 1
i = 0

while a < suma:
    fib.append(a)
    temp = a
    a = b
    b = temp + b
    i += 1


