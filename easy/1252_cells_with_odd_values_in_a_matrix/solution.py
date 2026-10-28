from collections import Counter


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows, cols = map(list, zip(*indices))

        rowsCounter = Counter(rows)
        colsCounter = Counter(cols)

        oddCount = 0

        for r in range(m):
            for c in range(n):
                if (rowsCounter.get(r, 0) + colsCounter.get(c, 0)) % 2 == 1:
                    oddCount += 1

        return oddCount
