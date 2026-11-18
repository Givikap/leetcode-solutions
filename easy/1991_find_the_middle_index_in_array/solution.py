class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for mid in range(len(nums)):
            rightSum -= nums[mid]

            if leftSum == rightSum:
                return mid

            leftSum += nums[mid]

        return -1
