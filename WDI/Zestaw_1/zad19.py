def factorial(n):
    if n == 0 or n == 1: return 1
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def calculate_e(prec = 10):
    e = 0
    for i in range(prec):  
        e += 1 / factorial(i)
    print(e)


calculate_e()
