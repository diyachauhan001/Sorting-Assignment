

def findRelativeRanks(nums):
    n = len(nums)
    ans = ["" for _ in range(n)]
    indices = list(range(n))

    indices.sort(key=lambda x: nums[x], reverse=True)

    for i in range(n):
        if i == 0:
            ans[indices[0]] = "Gold Medal"
        elif i == 1:
            ans[indices[1]] = "Silver Medal"
        elif i == 2:
            ans[indices[2]] = "Bronze Medal"
        else:
            ans[indices[i]] = str(i + 1)

    return ans


print(findRelativeRanks([5, 4, 3, 2, 1]))