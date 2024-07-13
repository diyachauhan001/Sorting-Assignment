from typing import List
def heightChecker( heights: List[int]) -> int:
    ans = 0
    currentHeight = 1
    count = [0] * 101

    for height in heights:
      count[height] += 1

    for height in heights:
      while count[currentHeight] == 0:
        currentHeight += 1
      if height != currentHeight:
        ans += 1
      count[currentHeight] -= 1

    return ans

print(heightChecker([1,1,4,2,1,3]))