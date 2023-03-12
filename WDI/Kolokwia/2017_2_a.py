def solve(t):
    i = 0
    max_length = 0
    length = 0
    sum = 0
    while i < len(t) - 1:
        if t[i + 1] > t[i]:
            sum = t[i]
            start = 0
            while t[i + 1] > t[i]:
                sum += t[i + 1]
            