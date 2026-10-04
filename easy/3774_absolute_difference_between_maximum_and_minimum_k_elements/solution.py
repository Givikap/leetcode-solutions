class Solution:
    def absDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[:k]) - sum(nums[len(nums) - k :]))
