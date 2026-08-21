from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 1

                i += 1

            if count >= p:
                right = mid
            else:
                left = mid + 1

        return left
