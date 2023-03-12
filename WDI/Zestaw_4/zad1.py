n = int(input())
steps = ((0, 1), (1 , 0), (0, -1), (-1, 0))
x, y = 0, 0
num = 1
t2 = [[0 for _ in range(n)] for _ in range(n)]
length = len(t2) - 1

while length > 0:
    for step in steps:
        a, b = step
        for i in range(length):
            t2[x][y] = num 
            x, y = x + a, y + b
            num += 1
    length -= 2
    x, y = x + 1, y + 1

if length == 0:
    t2[x][y] = num

for el in t2:
    print(el)
