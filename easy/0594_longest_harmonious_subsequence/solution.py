from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)

        maxLen = 0

        for num, count in numsCounter.items():
            if num + 1 in numsCounter:
                maxLen = max(maxLen, numsCounter[num] + numsCounter[num + 1])

        return maxLen
