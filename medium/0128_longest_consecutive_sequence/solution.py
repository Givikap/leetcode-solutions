from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLen = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            currLen = 1

            while num + 1 in numsSet:
                num += 1
                currLen += 1

            maxLen = max(maxLen, currLen)

        return maxLen
