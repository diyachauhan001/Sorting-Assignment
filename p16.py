from typing import List


def findDisappearedNumbers( nums: List[int]) -> List[int]:
    for num in nums:
      index = abs(num) - 1
      nums[index] = -abs(nums[index])

    return [i + 1 for i, num in enumerate(nums) if num > 0]

print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))