class Solution:
    def minElement(self, nums: list[int]) -> int:
        min_replacement = float("inf")

        for num in nums:
            replacement = 0

            while num:
                replacement += num % 10
                num //= 10

            min_replacement = min(min_replacement, replacement)

        return min_replacement
