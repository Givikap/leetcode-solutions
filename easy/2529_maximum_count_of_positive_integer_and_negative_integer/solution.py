class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positive_count = 0
        negative_count = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > 0:
                positive_count += 1
            else:
                break

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_count += 1
            else:
                break

        return max(positive_count, negative_count)
