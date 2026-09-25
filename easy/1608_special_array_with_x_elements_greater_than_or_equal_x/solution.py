class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()

        i = 0
        x = len(nums)

        while i < len(nums) and not nums[i]:
            i += 1
            x -= 1

        while x:
            if nums[i] >= x:
                return x
            elif x - 1 == nums[i]:
                break

            i += 1
            x -= 1

        return -1
