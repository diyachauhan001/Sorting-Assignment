from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    candidates = []

    for i, row in enumerate(mat):
      candidates.append([sum(row), i])

    candidates.sort(key=lambda c: (c[0], c[1]))

    return [i for _, i in candidates[:k]]

print(kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))