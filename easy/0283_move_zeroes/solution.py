class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        curr = 0

        for i in range(len(nums)):
            if not nums[i]:
                continue

            if curr < i:
                nums[curr], nums[i] = nums[i], nums[curr]

            curr += 1
