def A(x):
    return x + 3

def B(x):
    return 2 * x

def num_len(n):
    res = 0
    while n > 0:   
        res += 1
        n //= 10
    return res

def C(x):
    y = 0
    
