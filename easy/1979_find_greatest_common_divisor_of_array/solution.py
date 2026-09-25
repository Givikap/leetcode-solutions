import math


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        minNum = nums[0]
        maxNum = nums[0]

        for i in range(1, len(nums)):
            minNum = min(minNum, nums[i])
            maxNum = max(maxNum, nums[i])

        return math.gcd(minNum, maxNum)
