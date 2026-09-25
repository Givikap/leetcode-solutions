class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        differences = []

        numsSum = sum(nums)
        leftSum = 0

        for num in nums:
            differences.append(abs(leftSum * 2 + num - numsSum))
            leftSum += num

        return differences
