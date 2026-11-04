from statistics import median


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        med = int(median(nums))

        return sum(abs(num - med) for num in nums)
