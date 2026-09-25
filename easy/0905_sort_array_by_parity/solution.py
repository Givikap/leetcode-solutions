class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[even], nums[i] = nums[i], nums[even]
                even += 1

        return nums
