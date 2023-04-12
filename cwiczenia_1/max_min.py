#znalezc max, min przy pomocy 3/2n porownan

def solve(t):
    n = len(t)
    curr_min, curr_max = t[0]
    for i in range(1, n - 1, 2):
        if t[i] > t[i + 1]:
            curr_max = max(curr_max, t[i])
            curr_min = min(curr_min, t[i])
        else:
            curr_max = max(curr_max, t[i + 1])
            curr_min = min(curr_min, t[i + 1])
    if n % 2 == 0:
        curr_max = max(curr_max, t[n - 1])

# dana jest posorotwana tablica t z dodatnimi wartosciami oraz zadajemy
# liczbe x, znalezc takie 2 indeksy i, j, ze roznica t[j] - t[i] = x


def solve(t, target):
    n = len(t)
    i, j = 0, 1
    curr_val = t[j] - t[i]
    while curr_val != target:
        curr_val = t[j] - t[i]
        if i == n or j == n:
            return -1, -1
        if curr_val < target:
            j += 1
        elif curr_val > target:
            i += 1
        else:
            return i, j


print(solve([1, 3, 6, 8, 10], 5))

# posorotwany ciag liczb i elementy a0,...,an-1, wartosci ai to liczby 
# z zakresu [0, m-1] liczby w ciagu sa parami rozne 
# n < m najmniejsza liczba calkowita ktorej nie ma w tym ciagu


