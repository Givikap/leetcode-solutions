class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid == 0 or nums[mid - 1] < nums[mid]) and (
                mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
            ):
                return mid

            if (mid > 0 and nums[mid - 1] < nums[mid]) or (
                mid < len(nums) - 1 and nums[mid] < nums[mid + 1]
            ):
                left = mid + 1
            else:
                right = mid - 1

        return left
