from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums_counter = sorted(Counter(nums).items())

        for i in range(len(nums_counter)):
            for j in range(i + 1, len(nums_counter)):
                if nums_counter[i][1] != nums_counter[j][1]:
                    return [nums_counter[i][0], nums_counter[j][0]]

        return [-1, -1]
