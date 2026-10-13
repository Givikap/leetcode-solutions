class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = sorted(num**2 for num in nums)
        mid = len(nums) // 2
        return sum(nums[mid:]) - sum(nums[:mid])
