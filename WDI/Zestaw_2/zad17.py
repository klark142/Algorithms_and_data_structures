import math

def f(x):
    return x * math.log(x) - math.log(2020)

def df(x):
    return math.log(x) + 1

def solve(f, df):
    x = 1
    eps = 1e-4
    while abs(f(x)) > eps:
        x = x - f(x) / df(x)
    return x


print(solve(f, df))

