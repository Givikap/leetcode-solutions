from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        sequentialPrefixSum = nums[0]
        numsSet = {nums[0]}

        i = 1
        while i < n and nums[i - 1] + 1 == nums[i]:
            sequentialPrefixSum += nums[i]
            numsSet.add(nums[i])
            i += 1

        while i < n:
            numsSet.add(nums[i])
            i += 1

        while sequentialPrefixSum in numsSet:
            sequentialPrefixSum += 1

        return sequentialPrefixSum
