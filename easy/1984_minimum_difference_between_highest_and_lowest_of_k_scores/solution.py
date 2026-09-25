class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        min_diff = 100000

        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff
