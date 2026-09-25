class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        curr_ascending_sum = nums[0]
        max_ascending_sum = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr_ascending_sum += nums[i]
            else:
                max_ascending_sum = max(curr_ascending_sum, max_ascending_sum)
                curr_ascending_sum = nums[i]

        return max(curr_ascending_sum, max_ascending_sum)
