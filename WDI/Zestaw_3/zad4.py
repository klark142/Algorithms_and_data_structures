def zad4(n):
    digits = [1] + [0] * (n + 10)
    fact = 1
    k = 1
    while fact <= 10 ** n + 10:
        fact *= k
        k += 1
        long_div(1, fact, digits)
    for i in range(len(digits) - 1, 0, -1):
        digits[i - 1] += digits[i] // 10
        digits[i] %= 10
    return digits[:n]

def long_div(a, b, t):
    for i in range(1, len(t)):
        a *= 10
        t[i] += a // b
        a %= b
        if a == 0:
            return



