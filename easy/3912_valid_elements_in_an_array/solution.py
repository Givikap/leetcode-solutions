class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)

        prefix_maxes = [0] * nums_len
        suffix_maxes = [0] * nums_len

        for i, j in zip(range(1, nums_len), range(nums_len - 2, -1, -1)):
            prefix_maxes[i] = max(prefix_maxes[i - 1], nums[i - 1])
            suffix_maxes[j] = max(suffix_maxes[j + 1], nums[j + 1])

        valid_nums = [nums[0]]

        for i in range(1, nums_len - 1):
            if nums[i] > prefix_maxes[i] or nums[i] > suffix_maxes[i]:
                valid_nums.append(nums[i])

        if nums_len != 1:
            valid_nums.append(nums[-1])

        return valid_nums
