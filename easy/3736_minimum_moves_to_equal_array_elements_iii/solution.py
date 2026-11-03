class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxNum = max(nums)

        return sum(maxNum - num for num in nums)
