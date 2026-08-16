from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)

        maxLen = 1

        i = 1
        while i < n:
            currLen = 1

            while i < n and nums[i - 1] < nums[i]:
                currLen += 1
                i += 1

            maxLen = max(maxLen, currLen)
            i += 1

        return maxLen
