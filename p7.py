from typing import List

def sortedSquares( nums: List[int]) -> List[int]:
    n = len(nums)
    l = 0
    r = n - 1
    ans = [0] * n

    while n:
      n -= 1
      if abs(nums[l]) > abs(nums[r]):
        ans[n] = nums[l] * nums[l]
        l += 1
      else:
        ans[n] = nums[r] * nums[r]
        r -= 1

    return ans

print(sortedSquares([-4,-1,0,3,10]))