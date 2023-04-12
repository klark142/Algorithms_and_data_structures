# posortować liczby [0, .., n^2 - 1], gdzie n - długość tablicy - O(n)

# sortowanie stringów za pomocą radix sorta

from math import log10


def get_digit(num, i):
    num /= 10 ** i
    return num % 10


def sort(t, digit):
    n = len(t)
    B = [0] * n
    C = [0] * 10

    for i in range(n):
        C[get_digit(t[i], digit)] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[get_digit(t[i], digit) + 1]] = t[i]
        C[get_digit(t[i], digit)] -= 1


def radix(t):
    n = len(t)
    digit = 0
    max_length = int(log10(n ** 2 - 1)) + 1
    for i in range(max_length):
        sort(t, digit)
        digit += 1

    return t


t = [1, 5, 3, 2, 1, 10]
print(radix(t))


