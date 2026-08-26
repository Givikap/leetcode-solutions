from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numsSet = set(nums)

        m = k
        while m in numsSet:
            m += k

        return m
