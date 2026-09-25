from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        sorted_nums = []

        for num, count in sorted(
            Counter(nums).items(), key=lambda t: (t[1], -t[0])
        ):
            sorted_nums.extend([num] * count)

        return sorted_nums
