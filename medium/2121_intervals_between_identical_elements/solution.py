from collections import defaultdict


class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        indicesMap = defaultdict(list)
        for i, num in enumerate(arr):
            indicesMap[num].append(i)

        numsSums = [0] * len(arr)

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
