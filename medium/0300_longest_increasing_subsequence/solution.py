from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        for num in nums:
            if num > tails[-1]:
                tails.append(num)
            elif num < tails[-1]:
                tails[bisect_left(tails, num)] = num

        return len(tails)
