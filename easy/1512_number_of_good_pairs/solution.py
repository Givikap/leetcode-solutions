from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum(
            count * (count - 1) // 2 for count in Counter(nums).values()
        )
