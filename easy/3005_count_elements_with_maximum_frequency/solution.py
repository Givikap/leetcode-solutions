from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        nums_counter = defaultdict(int)

        max_frequency = 0
        max_frequency_count = 0

        for num in nums:
            nums_counter[num] += 1

            if nums_counter[num] > max_frequency:
                max_frequency = nums_counter[num]
                max_frequency_count = 1
            elif nums_counter[num] == max_frequency:
                max_frequency_count += 1

        return max_frequency * max_frequency_count
