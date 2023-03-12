import math 

def check(tab):
    mask = [False for _ in range(len(tab))]
    mask[0] = True

    for i, elem in enumerate(tab):
        if mask[i] == True:
            div = 2
            while elem > 1:
                while elem % div == 0:
                    if i + div < len(tab):
                        mask[i + div] = True
                    elem //= div
                div += 1
    return mask[-1]




tab = tuple(map(int, input().split()))
print(check(tab))
