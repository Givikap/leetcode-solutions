class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums_squared = [0] * len(nums)
        left, right = 0, len(nums) - 1
        i = right

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                nums_squared[i] = nums[left] ** 2
                left += 1
            else:
                nums_squared[i] = nums[right] ** 2
                right -= 1

            i -= 1

        return nums_squared
