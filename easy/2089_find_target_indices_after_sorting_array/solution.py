from bisect import bisect_left


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        nums.sort()

        i = bisect_left(nums, target)
        indices = []

        while i < n and nums[i] == target:
            indices.append(i)
            i += 1

        return indices
