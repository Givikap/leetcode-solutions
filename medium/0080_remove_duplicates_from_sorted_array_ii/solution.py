class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        insert = 2

        for read in range(2, len(nums)):
            if (
                nums[read] != nums[insert - 1]
                or nums[read] != nums[insert - 2]
            ):
                nums[insert] = nums[read]
                insert += 1

        return insert
