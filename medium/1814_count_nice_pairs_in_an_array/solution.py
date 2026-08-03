from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        pairsMap = defaultdict(int)

        for num in nums:
            numCopy = num
            numReversed = 0

            while numCopy:
                numReversed = numReversed * 10 + numCopy % 10
                numCopy //= 10

            pairsMap[num - numReversed] += 1

        MOD = 1000000007
        nicePairsCount = 0

        for count in pairsMap.values():
            nicePairsCount = (nicePairsCount + count * (count - 1) // 2) % MOD

        return nicePairsCount
