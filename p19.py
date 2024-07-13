from typing import List


def missingNumber( nums: List[int]) -> int:
    ans = len(nums)

    for i, num in enumerate(nums):
      ans ^= i ^ num

    return ans

print(missingNumber([3, 0, 1]))