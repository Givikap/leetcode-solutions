class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        numsLen = len(nums)

        i = 0
        while i < numsLen - 1 and nums[i] < nums[i + 1]:
            i += 1

        if i == 0 or i == numsLen - 1:
            return False

        while i < numsLen - 1 and nums[i] > nums[i + 1]:
            i += 1

        if i == numsLen - 1:
            return False

        while i < numsLen - 1 and nums[i] < nums[i + 1]:
            i += 1

        return i == numsLen - 1
