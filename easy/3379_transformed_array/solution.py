class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)
        return [nums[(i + num) % nums_len] for i, num in enumerate(nums)]
