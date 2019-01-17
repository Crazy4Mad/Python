def InsertionSort(A):
    for i in range(1, len(A)):
        for j in range(0, i, 1):
            if A[i] > A[j]:
                cur_elem = A[i]
                for k in range(j , i + 1):
                    A[k], cur_elem = cur_elem, A[k]
                break
    return A


A = InsertionSort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
