from collections import Counter


class Solution:
    def isGood(self, nums: list[int]) -> bool:
        nums_counter = Counter(nums)
        max_num = max(nums_counter)

        if nums_counter[max_num] != 2:
            return False

        for num in range(1, max_num):
            if nums_counter[num] != 1:
                return False

        return True
