class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evenIdx = 0
        oddIdx = 1

        i = 0
        while i < len(nums):
            if i % 2 == 0 and nums[i] % 2 == 1:
                nums[oddIdx], nums[i] = nums[i], nums[oddIdx]
                i -= 1
                oddIdx += 2
            elif i % 2 == 1 and nums[i] % 2 == 0:
                nums[evenIdx], nums[i] = nums[i], nums[evenIdx]
                i -= 1
                evenIdx += 2

            i += 1

        return nums
