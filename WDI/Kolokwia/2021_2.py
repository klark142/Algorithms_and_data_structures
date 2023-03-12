def base_4(num):
    res = 0
    mult = 1
    while num > 0:
        res += (num % 4) * mult
        num //= 4
        mult *= 10
    return res
    

def zbior_cyfr(a, b):
    t_a = [0 for _ in range(10)]
    t_b = [0 for _ in range(10)]
    while a > 0:
        last = a % 10
        if t_a[last] != 1:
            t_a[last] += 1
        a //= 10
    while b > 0:
        last = b % 10
        if t_b[last] != 1:
            t_b[last] += 1
        b //= 10
    for i in range(len(t_a)):
        if t_a[i] != t_b[i]:
            return False
    return True

def zgodne_4(a, b):
    return zbior_cyfr((base_4(a)), base_4(b))



def solve(t):
    curr_highest = 0
    highest = 0
    for i in range(len(t)):
        curr_highest = 0
        for j in range(len(t)):
            if zgodne_4(t[i], t[j]) and i != j:  
                curr_highest += 1
        if curr_highest > highest:
            highest = curr_highest
    if highest == 0:
        return highest
    if highest > 0:
        return highest + 1


print(solve([13, 23, 18, 87, 33, 2]))

            

