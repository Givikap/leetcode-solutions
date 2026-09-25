from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = bisect_left(nums, target)

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, bisect_right(nums, target) - 1]
