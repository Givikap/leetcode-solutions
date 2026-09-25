class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:
        groupsMap = [0] * n
        currGroup = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                currGroup += 1

            groupsMap[i] = currGroup

        return [groupsMap[i] == groupsMap[j] for i, j in queries]
