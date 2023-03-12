def suma_dzielnikow(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

for x in range(1, 1000001):
    for y in range(1, 1000001):
        sum_x = suma_dzielnikow(x)
        sum_y = suma_dzielnikow(y)

        if sum_x == y and sum_y == x and x != y:
            print(x, y)


