class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[mid] < target:
            while mid < len(nums) and nums[mid] < target:
                mid += 1

            return mid
        else:
            while mid >= 0 and nums[mid] > target:
                mid -= 1

            return mid + 1
