from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        numsCounter = defaultdict(int)

        left = 0
        right = 0

        maxLen = 0

        while right < n:
            num = nums[right]

            if numsCounter[num] < k:
                numsCounter[num] += 1
                right += 1
            else:
                while numsCounter[num] == k:
                    numsCounter[nums[left]] -= 1
                    left += 1

            maxLen = max(maxLen, right - left)

        return maxLen
