class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while True:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            if start >= end:
                return -1

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
