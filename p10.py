def targetIndices(nums, target):
    sorted_nums = sorted(nums)

    target_indices = []
    for i in range(len(sorted_nums)):
        if sorted_nums[i] == target:
            target_indices.append(i)

    return target_indices


print(targetIndices([1, 2, 5, 2, 3], 2))
