from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        numsCounter = Counter(nums)

        maxLen = 0

        for num, count in numsCounter.items():
            if num + 1 in numsCounter:
                maxLen = max(maxLen, numsCounter[num] + numsCounter[num + 1])

        return maxLen
