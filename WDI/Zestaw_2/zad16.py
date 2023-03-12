from math import isqrt

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def factorization(num):
    fact = []
    for i in range (2, num + 1):
        while num % i == 0:
            fact.append(i)
            num = num / i
    return fact
#sum digits of numbers in array to do

def sum_of_digitis_in_arr(fact):
    sum = 0
    for number in fact:
        while number > 0:
            sum += number % 10
            number = number // 10
    return sum


for number in range(2, 1_000_000):
    arr = factorization(number)
    sum = sum_of_digitis_in_arr(arr)
    if sum == sum_of_digits(number):
        print(number)

