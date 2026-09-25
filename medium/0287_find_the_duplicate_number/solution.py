class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        sorted_unique_nums = list(range(1, len(nums) + 1))

        for num in nums:
            if sorted_unique_nums[num - 1] == -1:
                return num

            sorted_unique_nums[num - 1] = -1
