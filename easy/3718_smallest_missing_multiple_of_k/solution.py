class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        numsSet = set(nums)

        m = k
        while m in numsSet:
            m += k

        return m
