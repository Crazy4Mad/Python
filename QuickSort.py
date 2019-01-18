def quicksort(nums):
        if len(nums) <= 1:
            return nums
        else:
            q = nums[int(len(nums) / 2)]
        l_nums, b_nums = [], []
        e_nums = 0

        for number in nums:
            if number > q: l_nums += [number]
            elif number < q: b_nums += [number]
            else: e_nums += 1

        return quicksort(l_nums) + e_nums*[q] + quicksort(b_nums)


A = quicksort([int(aux) for aux in input().split()])
for i in A:
    print(i, end=' ')
