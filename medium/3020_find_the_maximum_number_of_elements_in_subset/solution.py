from collections import Counter


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        numsCounter = Counter(nums)

        if 1 in numsCounter:
            maxLen = numsCounter.pop(1)
            if maxLen % 2 == 0:
                maxLen -= 1
        else:
            maxLen = 0

        for num in numsCounter.keys():
            currLen = 0

            while numsCounter.get(num, 0) >= 2:
                num *= num
                currLen += 2

            if numsCounter.get(num, 0) == 1:
                maxLen = max(maxLen, currLen + 1)
            else:
                maxLen = max(maxLen, currLen - 1)

        return maxLen
