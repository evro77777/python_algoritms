def insertSort(A):
    """Сортировка списка А вставками"""
    for k in range(1, len(A)):
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1
    return A


print(insertSort([4, 3, 2, 5, 1]))
