from collections import Counter


class Solution:
    def findLucky(self, nums: list[int]) -> int:
        return max(
            [num for num, count in Counter(nums).items() if num == count],
            default=-1,
        )
