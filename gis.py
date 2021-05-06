def gis(A):
    F = [0] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1
        print(i,F)
    return F
print(gis([3,4,1,7]))