def min_suma(T):
    n = len(T)
    def rek(i=0, sum_e=0, sum_i=0, cnt=0):
        if i == n:
            if sum_e == sum_i:
                return sum_e, cnt
            return float('inf'), float('inf')
        a = rek(i + 1, sum_e, sum_i, cnt)
        b = rek(i + 1, sum_e + T[i], sum_i + i, cnt + 1)
        if a[1] < b[1]:
            return a
        return b
    return rek()[0]

print(min_suma([1, 7, 3, 5, 11, 2]))