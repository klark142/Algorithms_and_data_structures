a, b = map(int, input().split())
n = int(input('Jaka dokladnosc? '))
t = [0 for _ in range(n)]
t[0] = a // b
for i in range(1, n): 
    a = a * 10
    t[i] += a // b
    a = a % b

print(f'{a//b},', end = '')
for i in range(1, n):
    print(t[i], end='')

