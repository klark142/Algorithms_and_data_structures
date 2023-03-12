def is_valid(a, b):
    tab_a = [0 for _ in range(10)]
    tab_b = [0 for _ in range(10)]
    while a > 0:
        last_a = a % 10
        if tab_a[last_a] != 1: 
            tab_a[last_a] += 1
        a //= 10
    while b > 0:
        last_b = b % 10
        if tab_b[last_b] != 1:
            tab_b[last_b] += 1
        b //= 10
    for i in range(10):
        if tab_a[i] != tab_b[i]:
            return False
    return True
    
t2 = [
    [1,2,0,4,5],
    [1,1,2,0,34],
    [2,4,0,1,0],
    [3,0,1,27,3],
    [0,1,0,16,1]
]

