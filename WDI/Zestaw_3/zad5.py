def find_10th_biggest(numbers):
    no_duplicates = []
    for number in numbers:
        if number not in no_duplicates:
            no_duplicates.append(number)
    no_duplicates.sort(reverse=True)
    return no_duplicates[11]



numbers = list(map(int, input().split()))
print(find_10th_biggest(numbers))
