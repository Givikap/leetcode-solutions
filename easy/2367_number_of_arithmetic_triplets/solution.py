class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n = len(nums)

        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] != diff:
                    continue

                for k in range(j + 1, n):
                    if nums[k] - nums[j] == diff:
                        count += 1

        return count
