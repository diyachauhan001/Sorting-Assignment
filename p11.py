import itertools
from typing import List

def specialArray(nums: List[int]) -> int:
    nums.sort()

    if nums[0] >= len(nums):
      return len(nums)

    for i, (a, b) in enumerate(itertools.pairwise(nums)):
      count = len(nums) - i - 1
      if a < count and b >= count:
        return count

    return -1

print(specialArray([3, 6, 7, 7, 0]))