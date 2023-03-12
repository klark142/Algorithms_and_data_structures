a, b = map(int, input('Podaj poczatkowe wyrazy ciagu fib: ').split())
prec = int(input('Precision: '))

for i in range(prec):
    temp = a
    a = b
    b = temp + b

div = a / b

print(div)
    