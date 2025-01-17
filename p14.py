
import collections
import heapq
from typing import List


class T:
  def __init__(self, num: int, freq: int):
    self.num = num
    self.freq = freq

  def __lt__(self, other):
    if self.freq == other.freq:
      return self.num > other.num
    return self.freq < other.freq


def frequencySort( nums: List[int]) -> List[int]:
    ans = []
    heap = []

    for num, freq in collections.Counter(nums).items():
      heapq.heappush(heap, T(num, freq))

    while len(heap) > 0:
      num = heap[0].num
      freq = heapq.heappop(heap).freq
      ans.extend([num] * freq)

    return ans

print(frequencySort([1, 1, 2, 2, 2, 3]))