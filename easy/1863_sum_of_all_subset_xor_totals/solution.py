from functools import reduce


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x | y, nums) * (2 ** (len(nums) - 1))
