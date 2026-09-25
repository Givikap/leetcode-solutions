class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        subsets_list = [[]]
        last_size = 0

        for i in range(len(nums)):
            start = last_size if i > 0 and nums[i - 1] == nums[i] else 0
            last_size = len(subsets_list)

            for j in range(start, len(subsets_list)):
                subsets_list.append(subsets_list[j] + [nums[i]])

        return subsets_list
