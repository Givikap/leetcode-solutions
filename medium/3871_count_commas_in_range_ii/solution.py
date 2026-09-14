class Solution:
    def countCommas(self, n: int) -> int:
        commasCount = 0

        bound = 1000
        multiplier = 1

        while bound <= n:
            commasCount += (min(bound * 1000 - 1, n) - bound + 1) * multiplier
            bound *= 1000
            multiplier += 1

        return commasCount
