class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:
        uniqueSortedVals = sorted(set(nums))
        indicesMap = {val: i for i, val in enumerate(uniqueSortedVals)}

        m = len(uniqueSortedVals)

        groupsMap = [0] * m
        currGroup = 0

        for i in range(1, m):
            if uniqueSortedVals[i] - uniqueSortedVals[i - 1] > maxDiff:
                currGroup += 1

            groupsMap[i] = currGroup

        maxHops = max(1, m.bit_length())

        jumps = [None] * maxHops
        jumps0 = [0] * m

        right = 0

        for i in range(m):
            while (
                right + 1 < m
                and uniqueSortedVals[right + 1]
                <= uniqueSortedVals[i] + maxDiff
            ):
                right += 1
            jumps0[i] = right

        jumps[0] = jumps0

        for h in range(1, maxHops):
            jumps[h] = [jumps[h - 1][jumps[h - 1][i]] for i in range(m)]

        pathsExist = []

        for u, v in queries:
            if u == v:
                pathsExist.append(0)
                continue

            uVal, vVal = nums[u], nums[v]
            if uVal == vVal:
                pathsExist.append(1)
                continue

            if uVal > vVal:
                uVal, vVal = vVal, uVal

            uIdx, vIdx = indicesMap[uVal], indicesMap[vVal]

            if groupsMap[uIdx] != groupsMap[vIdx]:
                pathsExist.append(-1)
                continue

            curr = uIdx
            hops = 0

            for h in range(maxHops - 1, -1, -1):
                if jumps[h][curr] < vIdx:
                    curr = jumps[h][curr]
                    hops += 1 << h

            pathsExist.append(hops + 1)

        return pathsExist
