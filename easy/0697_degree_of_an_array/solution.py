from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        numsCounter = Counter(nums)

        maxCount = max(numsCounter.values())
        if maxCount == 1:
            return 1

        numsLen = len(nums)
        minLen = numsLen

        for num, count in numsCounter.items():
            if count == maxCount:
                left = nums.index(num)
                right = numsLen - nums[::-1].index(num) - 1

                minLen = min(minLen, right - left + 1)

        return minLen
