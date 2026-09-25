from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for num, count in Counter(nums).items():
            if count == 1 and num % 2 == 0:
                return num

        return -1
