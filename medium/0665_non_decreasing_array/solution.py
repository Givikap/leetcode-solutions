class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        modified = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                else:
                    modified = True

                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]

        return True
