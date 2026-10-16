class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)

        countSquaresSum = 0

        for i in range(n):
            seen = [False] * 101
            distinctCount = 0

            for j in range(i, n):
                if not seen[nums[j]]:
                    seen[nums[j]] = True
                    distinctCount += 1

                countSquaresSum += distinctCount * distinctCount

        return countSquaresSum
