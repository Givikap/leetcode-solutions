from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        numsCounter = Counter(nums)

        if k == 1:
            maxNum = -1

            for num, count in numsCounter.items():
                if count == 1:
                    maxNum = max(maxNum, num)

            return maxNum

        if numsCounter[nums[0]] == 1 and numsCounter[nums[-1]] == 1:
            return nums[0] if nums[0] > nums[-1] else nums[-1]
        elif numsCounter[nums[0]] == 1:
            return nums[0]
        elif numsCounter[nums[-1]] == 1:
            return nums[-1]

        return -1
