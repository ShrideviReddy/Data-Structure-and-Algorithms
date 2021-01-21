def two_sum(nums, sum_to_find):
    required = {}
    for i in range(len(nums)):
        if (sum_to_find-nums[i]) in required:
            return [required[sum_to_find-nums[i]], i]
        else:
            required[nums[i]] = i

index_of_pair = two_sum([1,1,2,3], 5)
print(index_of_pair)
