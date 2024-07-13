from typing import List


def findDuplicates( nums: List[int]) -> List[int]:
    ans = []

    for num in nums:
      nums[abs(num) - 1] *= -1
      if nums[abs(num) - 1] > 0:
        ans.append(abs(num))

    return ans

print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))