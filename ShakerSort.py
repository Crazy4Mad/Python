def BubbleSort(A):
    change = True
    left, right = 0, len(A) - 1
    while left < right and change:
        change = False
        for i in range(left, right):
            if A[i] < A[i + 1]:
                change = True
                A[i], A[i + 1] = A[i + 1], A[i]
        right -= 1
        if not change:
            break
        for i in range(right, left, -1):
            if A[i] > A[i - 1]:
                change = True
                A[i], A[i - 1] = A[i - 1], A[i]
        left += 1
    return A


A = BubbleSort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
