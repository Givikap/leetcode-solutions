class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        min_difference = float("inf")

        prev_num = 0
        prev_i = 0

        for i, num in enumerate(nums):
            if num == 0:
                continue

            if prev_num == 3 - num and i - prev_i < min_difference:
                min_difference = i - prev_i

            prev_num = num
            prev_i = i

        return min_difference if min_difference != float("inf") else -1
