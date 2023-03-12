def solve(t):
    sub_count = 0
    sub_length = 1
    for ind in range(len(t) - 1):
        if t[ind + 1] > t[ind]:
            sub_length += 1
            if sub_length == 3:
                sub_count += 1
        else:
            sub_length = 1
    start = [0 for _ in range(sub_count)]
    end = [0 for _ in range(sub_count)]
    sub_count = 0
    sub_length = 1
    for ind in range(len(t) - 1):
        if t[ind + 1] > t[ind]:
            sub_length += 1
            if sub_length == 3:
                start[sub_count] = t[ind - 1]
                sub_count += 1
        else:
            if sub_length > 2:
                end[sub_count - 1] = t[ind]
            sub_length = 1
    return min(end) < max(start)

def solve2(t):
    sub_length = 1
    min_end = float('inf')
    max_start = 0
    for ind in range(len(t) - 1):
        if t[ind + 1] > t[ind]:
            sub_length += 1
            if sub_length == 3:
                max_start = max(max_start, t[ind - 1])
        else:
            if sub_length > 2:
                min_end = min(min_end, t[ind])
            sub_length = 1
    return min_end < max_start
            
    

print(solve2([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))

        
        