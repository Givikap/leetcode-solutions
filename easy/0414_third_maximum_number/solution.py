class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort()

        count = 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                if count == 2:
                    return nums[i - 1]

                count += 1

        return nums[-1]
