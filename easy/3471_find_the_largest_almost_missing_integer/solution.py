from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        numsCounter = Counter(nums)

        return max(
            (
                num
                for num in (
                    numsCounter.keys() if k == 1 else (nums[0], nums[-1])
                )
                if numsCounter[num] == 1
            ),
            default=-1,
        )
