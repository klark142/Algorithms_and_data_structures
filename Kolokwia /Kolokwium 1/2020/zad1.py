def covert(num):
    jednokrotne = 0
    wielokrotne = 0
    count_arr = [0 for _ in range(10)]
    temp = num
    while temp > 0:
        digit = temp % 10
        count_arr[digit] += 1
        temp //= 10

    for i in range(10):
        if count_arr[i] == 1:
            jednokrotne += 1
        elif count_arr[i] > 1:
            wielokrotne += 1

    return num, jednokrotne, wielokrotne


def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        left = T[:mid]
        right = T[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1] or (left[i][1] == right[j][1] and left[i][2] < right[j][2]):
                T[k] = left[i]
                i += 1
            else:
                T[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            T[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            T[k] = right[j]
            j += 1
            k += 1

    return T


def pretty_sort(T):
    for i in range(len(T)):
        T[i] = covert(T[i])

    res = []
    T = merge_sort(T)
    for i, j, k in T:
        res.append(i)

    return res


print(pretty_sort([123, 455, 1266, 1266, 455, 2344, 67333]))
