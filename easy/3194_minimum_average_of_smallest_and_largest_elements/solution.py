from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1

        minAverage = float("inf")

        while left <= right:
            minAverage = min(minAverage, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1

        return minAverage
