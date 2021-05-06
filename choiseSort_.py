def choise_sort(A):
    """Сортировка списка А выбором"""
    for pos in range(0, len(A)-1):
        for k in range(pos+1, len(A)):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


print(choise_sort([4, 3, 2, 5, 1])) 