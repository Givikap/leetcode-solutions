class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rowsCounter = [0] * m
        colsCounter = [0] * n

        for r, c in indices:
            rowsCounter[r] += 1
            colsCounter[c] += 1

        return sum(
            [
                (rowsCounter[r] + colsCounter[c]) % 2
                for r in range(m)
                for c in range(n)
            ]
        )
