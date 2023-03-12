def is_palindrome(num):
    temp = num
    reverse = 0
    while num > 0:
        reverse = reverse * 10
        reverse += num % 10
        num = num // 10
    if temp == reverse:
        return True
    return False

def to_binary(num):
    binary = 0
    exp = 1
    while num > 0:
        binary += (num % 2) * exp
        num = num // 2
        exp *= 10
    return binary

num = int(input())
print(is_palindrome(num))
print(is_palindrome(to_binary(num)))




#n = int(input())
#print(is_palindrome(n))
