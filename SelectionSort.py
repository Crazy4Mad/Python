def SelectionSort(A):
    for i in range(len(A)):
        max_ind = i
        for j in range(i, len(A)):
            if A[max_ind] < A[j]:
                max_ind = j
        A[max_ind], A[i] = A[i], A[max_ind]
    return A


A = SelectionSort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
