for num in range(4, 1000001, 2):
    sum = 0
    for i in range(1, num):   
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)


