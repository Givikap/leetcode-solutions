class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ones_count = 0
        max_ones_count = 0

        for num in nums:
            if num:
                ones_count += 1
            else:
                max_ones_count = max(max_ones_count, ones_count)
                ones_count = 0

        return max(max_ones_count, ones_count)
