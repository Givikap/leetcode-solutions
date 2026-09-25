class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        sortedUniqueNums = sorted(set(nums))

        n = len(nums)
        m = len(sortedUniqueNums)

        rankMap = {}
        for i, num in enumerate(sortedUniqueNums):
            rankMap[num] = i + 1

        fenwickTree = [0] * (m + 1)

        def query(i: int) -> int:
            fenwickSum = 0

            while i:
                fenwickSum += fenwickTree[i]
                i -= i & (-i)

            return fenwickSum

        def update(i: int):
            while i <= m:
                fenwickTree[i] += 1
                i += i & (-i)

        counts = [0] * n

        for i in range(len(nums) - 1, -1, -1):
            rank = rankMap[nums[i]]
            counts[i] = query(rank - 1)
            update(rank)

        return counts
