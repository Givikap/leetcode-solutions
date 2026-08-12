from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = [[0] * (n + 1) for _ in range(n)]

        suffixSums = [piles[-1]] * n
        for i in range(n - 2, -1, -1):
            suffixSums[i] = piles[i] + suffixSums[i + 1]

        def solve(i: int, m: int) -> int:
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffixSums[i]
            if dp[i][m] != 0:
                return dp[i][m]

            stones = float("inf")

            for x in range(1, 2 * m + 1):
                stones = min(stones, solve(i + x, max(m, x)))

            dp[i][m] = suffixSums[i] - stones
            return dp[i][m]

        return solve(0, 1)
