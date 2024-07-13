from typing import List

def numberGame(nums: List[int]) -> List[int]:
    nums.sort()
    return [nums[i + 1] if i % 2 == 0
            else nums[i - 1]
            for i in range(len(nums))]
    
print(numberGame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))