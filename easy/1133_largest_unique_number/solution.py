from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        largest_unique_num = -1

        for num, count in Counter(nums).items():
            if count == 1:
                largest_unique_num = max(num, largest_unique_num)

        return largest_unique_num
