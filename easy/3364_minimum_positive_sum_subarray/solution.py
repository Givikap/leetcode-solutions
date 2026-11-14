class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)

        prefixSums = [0] * (n + 1)
        for i in range(n):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        minSum = float("inf")

        for s in range(l, r + 1):
            for i in range(n - s + 1):
                currSum = prefixSums[i + s] - prefixSums[i]

                if currSum > 0:
                    minSum = min(minSum, currSum)

        return -1 if minSum == float("inf") else minSum
