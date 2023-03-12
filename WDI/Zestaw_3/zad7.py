import random 

def only_odd_numbers(t):
    found = False
    while not found:    
        for number in t:
            while not found:
                if (number % 10) % 2 == 0:
                    break
                else:
                    number //= 10
                    if number == 0:
                        found = True
                        return True
    return False

n = int(input())
t = [random.randint(1, 1000) for _ in range(n)]

print(only_odd_numbers(t))

