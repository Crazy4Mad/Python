def InsertionSort(A):
    for i in range(1, len(A)):
        left, right = 0, i - 1
        while left <= right:
            middle = (left + right) // 2
            if A[middle] < A[i]:
                right = middle - 1
            else:
                left = middle + 1
        A.insert(left, A.pop(i))
    return A


A = InsertionSort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
