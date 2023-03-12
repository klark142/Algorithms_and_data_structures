def is_prime(n):
    if n == 1:
        return False 
    if n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False 
    i = 5
    while i * i <= n:
        if n % i or n % (i + 2) == 0:
            return False 
        i = i + 6
    return True

def check(t):
    a, b = 1, 1
    prime = False
    for i in range(len(t)):
        if i == a:
            #check composite
            if is_prime(t[i]) or t[i] == 1:
                return False
            a, b = b, a + b
        if i != a and not prime:
            if is_prime(t[i]):
                prime = True
    return prime

t = list(map(int, input().split()))
print(check(t))

