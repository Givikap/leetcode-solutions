from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indicesMap = defaultdict(list)
        for i, num in enumerate(nums):
            indicesMap[num].append(i)

        numsSums = [0] * len(nums)

        for indices in indicesMap.values():
            k = len(indices)

            indicesSum = sum(indices)
            leftSum = 0

            for m, index in enumerate(indices):
                numsSums[index] = (
                    indicesSum - 2 * leftSum - index * (k - 2 * m)
                )
                leftSum += index

        return numsSums
