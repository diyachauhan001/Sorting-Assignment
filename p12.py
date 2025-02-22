from typing import List
import math


def buyChoco( prices: List[int], money: int) -> int:
    min1 = math.inf
    min2 = math.inf

    for price in prices:
      if price <= min1:
        min2 = min1
        min1 = price
      elif price < min2:
        min2 = price

    minCost = min1 + min2
    return money if minCost > money else money - minCost

print(buyChoco([1, 2, 3], 6))