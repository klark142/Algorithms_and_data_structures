def nwd_2(a, b):
    while b:
        a, b = b, a % b
    return a

def is_valid(a, b, c):
    return nwd_2(a, b) == nwd_2(b, c) == nwd_2(a, c) == 1

def solve(t):
    count = 0 
    gaps = [(1, 2), (2, 4), (1, 3), (2, 3)]
    for gap1, gap2 in gaps:    
        for i in range(len(t) - gap2):
            if is_valid(t[i], t[i + gap1], t[i + gap2]):
                print(t[i], t[i + gap1], t[i + gap2])
                count += 1
    return count



t = [2,3,4,5,6,8,7]
print(solve(t))