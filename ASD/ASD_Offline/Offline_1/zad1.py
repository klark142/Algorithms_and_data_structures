from zad1testy import runtests


def ceasar(s):
    left = 0
    right = float("-inf")
    n = len(s)
    p_lengths = [0] * n  # tablica, której wartość p_lengths[i] odpowiada maksymalnej długości palindromu o środku s[i]
    for i in range(n):
        # zmniejszenie liczby porównań poprzez sprawdzanie, czy rozważany palindrom zawiera się w innym palindromie i
        # można przypisać mu już początkową długość
        if left <= i <= right:  # jeśli i zawiera się w [left, right]
            mirror_index = left + right - i
            p_lengths[i] = min(p_lengths[mirror_index],
                               right - i)  # max długość palindromu o środku s[i] ograniczona z góry przez right - i
            # do końca przedziału [left, right]

        curr_left = i - p_lengths[i] - 1
        curr_right = i + p_lengths[i] + 1

        while curr_left >= 0 and curr_right < n and s[curr_left] == s[curr_right]:
            p_lengths[i] += 1
            curr_left -= 1
            curr_right += 1

        if i + p_lengths[i] > right:
            left = i - p_lengths[i]
            right = i + p_lengths[i]

    return (max(p_lengths) * 2) + 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar, all_tests=True)
