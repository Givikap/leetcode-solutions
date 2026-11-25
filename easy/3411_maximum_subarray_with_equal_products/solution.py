from math import gcd, lcm


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)

        maxLen = 1

        for i in range(n):
            subarrayProduct = 1
            subarrayGcd = 0
            subarrayLcm = 1

            for j in range(i, n):
                subarrayProduct *= nums[j]
                subarrayGcd = gcd(subarrayGcd, nums[j])
                subarrayLcm = lcm(subarrayLcm, nums[j])

                if subarrayProduct == subarrayGcd * subarrayLcm:
                    maxLen = max(maxLen, j - i + 1)

        return maxLen
