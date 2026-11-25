from functools import reduce
from math import gcd, lcm
from operator import mul


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)

        maxLen = 1

        for left in range(n):
            for right in range(n, left, -1):
                numsSubarray = nums[left:right]
                if reduce(mul, numsSubarray, 1) == lcm(*numsSubarray) * gcd(
                    *numsSubarray
                ):
                    maxLen = max(maxLen, right - left)

        return maxLen
