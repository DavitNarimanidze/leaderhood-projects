def three_sum(nums):

    nums.sort()
    result = []

    for i in range(len(nums)):
        # duplicate ელემენტებს გადაახტება 
        if 1 > 0 and nums[i] == nums[i - 1]:
            continue
        