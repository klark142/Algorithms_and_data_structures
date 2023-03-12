from random import randint

def only_odd(num):
    while num > 0:
        last = num % 10
        if last % 2 == 0:
            return False
        num //= 10
    return True

def check(t2):
    row = 0
    col = 0
    for _ in range(len(t2)):
        while col < len(t2):
            if only_odd(t2[row][col]):
                row += 1
                col = 0
            col += 1
            if row == len(t2):
                return False
        return True
        

#n = int(input('Liczba wierszy i kolumn: '))
#t2 = [[randint(1, 100) for _ in range(n)] for _ in range(n)]
t2 = [
    [2,2,22,44,44],
    [1,1,1,9,39],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]

print(check(t2))



    

