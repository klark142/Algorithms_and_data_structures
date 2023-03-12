from random import randint

def bubble_sort(t2):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(t2) - 1):
            if t2[i] > t2[i + 1]:
                t2[i], t2[i + 1] = t2[i + 1], t2[i]
                sorted = False
    return t2


def delete_duplicates(t2):
    no_duplicates = []
    for number in t2:
        if number not in no_duplicates:
            no_duplicates.append(number)
    return no_duplicates


n = int(input('Liczba wierszy i kolumn: '))
t1 = [[randint(1, 100) for _ in range(n)] for _ in range(n)]
t2 = []

for i in range(n):
    for j in range(n):
        t2.append(t1[i][j])

bubble_sort(t2)
print(delete_duplicates(t2))


