from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        pairsMap = defaultdict(int)

        pairsCount = n * (n - 1) // 2
        goodPairsCount = 0

        for i in range(n):
            goodPairsCount += pairsMap[i - nums[i]]
            pairsMap[i - nums[i]] += 1

        return pairsCount - goodPairsCount
