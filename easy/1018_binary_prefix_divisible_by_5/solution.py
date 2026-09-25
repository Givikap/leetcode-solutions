class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        val = 0

        for i in range(len(nums)):
            val = (val * 2 + nums[i]) % 5
            nums[i] = val == 0

        return nums
