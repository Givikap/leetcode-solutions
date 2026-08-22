from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0] * cols

        prev = 0
        maxSize = 0

        for row in range(rows):
            for col in range(cols):
                temp = dp[col]

                if row == 0 or col == 0 or matrix[row][col] == "0":
                    dp[col] = int(matrix[row][col] == "1")
                else:
                    dp[col] = min(prev, dp[col], dp[col - 1]) + 1

                prev = temp
                maxSize = max(maxSize, dp[col])

        return maxSize * maxSize
