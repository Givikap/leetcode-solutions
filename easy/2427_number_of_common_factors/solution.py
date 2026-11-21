class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 1

        for factor in range(2, min(a, b) + 1):
            if a % factor == 0 and b % factor == 0:
                count += 1

        return count
