from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow = nums[nums[0]]
    fast = nums[nums[nums[0]]]

    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    slow = nums[0]

    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]

    return slow

print(findDuplicate([1, 3, 4, 2, 2]))