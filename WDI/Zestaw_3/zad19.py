def check(t):
    i1, i2 = 0, 1
    max = 0
    while i1 < len(t) - 1 and i2 < len(t):    
        curr_max = 0
        while t[i1] - t[i2] < 0:
            #sum of elements
            sum_elem = 0
            n = i2 - i1 + 1
            for i in range(i1, i2 + 1):
                sum_elem += t[i]
            if (i1 + i2) / 2 * n == sum_elem:
                curr_max = n
            i2 += 1
        if curr_max > max:
            max = curr_max
        i1, i2 = i1 + 1, i1 + 2
    return max

t = list(map(int, input().split()))
print(check(t))

