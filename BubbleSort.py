def BubbleSort(A):
    change = True
    for j in range(len(A) - 1):
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                change = True
                A[i], A[i + 1] = A[i + 1], A[i]
    return A


A = BubbleSort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
