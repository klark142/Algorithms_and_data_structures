def counting_sort(A, k):
    n = len(A)
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(n)]

    for j in range(n):
        C[A[j]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        pass