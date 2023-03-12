def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def wzglednie_pierwsze(a, b):
    return nwd(a, b) == 1

def num_len(num):
    res = 0
    while num > 0:
        res += 1
        num //= 10
    return res

def solve(N):
    def recur(N, a=0, b=0, lenA=0, lenB=0):
        if N == 0:
            if wzglednie_pierwsze(a, b):
                print((a, b))
            return
        #biorę do liczby a
        recur(N // 10, a + (N % 10) * 10 ** lenA, b, lenA + 1, lenB)
        #biorę do liczby b
        recur(N // 10, a, b + (N % 10) * 10 ** lenB, lenA, lenB + 1)
    recur(N)

solve(21523)
        



