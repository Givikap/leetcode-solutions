from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)

        if (numsSum + target) % 2 == 1 or abs(target) > numsSum:
            return 0

        capacity = (numsSum + target) // 2

        dp = [0] * (capacity + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(capacity, -1, -1):
                if j < nums[i]:
                    break

                dp[j] += dp[j - nums[i]]

        return dp[capacity]
