from argparse import _MutuallyExclusiveGroup


def check(t):
    max, min = 0, 0
    for i in range(len(t)):
        if t[i] > max:
            max = t[i]
        if t[i] < min:
            min = t[i]
    max_count = 0
    min_count = 0
    for j in range(len(t)):
        if t[j] == max:
            max_count += 1
        if t[j] == min:
            min_count += 1
    return max_count == 1 and min_count == 1


t = list(map(int, input().split()))
print(check(t))
