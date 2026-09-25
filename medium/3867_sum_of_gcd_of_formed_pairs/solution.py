import math


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        currMax = 0
        prefixGcd = []

        for num in nums:
            currMax = max(currMax, num)
            prefixGcd.append(math.gcd(num, currMax))

        prefixGcd.sort()

        gcdSum = 0

        for i in range(n // 2):
            gcdSum += math.gcd(prefixGcd[i], prefixGcd[n - i - 1])

        return gcdSum
