def divisors(num: int) -> list:
    factor = 2
    tab = []
    while num != 1:
        if num % factor == 0:
            tab += [factor]
        while num % factor == 0:
            num //= factor
        factor += 1
    return tab

def solve(num):
    t = divisors(num)
    def recursion(t, il, i=0):
        if i == len(t):
            s += il
            return
        recursion()


