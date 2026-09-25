class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[], *[[num] for num in nums]]

        subsets_list = [[]]

        for num in nums:
            for i in range(len(subsets_list)):
                subsets_list.append(subsets_list[i] + [num])

        return subsets_list
