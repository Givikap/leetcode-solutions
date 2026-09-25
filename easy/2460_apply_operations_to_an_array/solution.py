class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)
        nums_copy = nums

        nums = []

        zero_count = 0
        i = 0

        while i < nums_len:
            if nums_copy[i] == 0:
                zero_count += 1
            elif i < nums_len - 1 and nums_copy[i] == nums_copy[i + 1]:
                nums.append(nums_copy[i] * 2)

                zero_count += 1
                i += 1
            else:
                nums.append(nums_copy[i])

            i += 1

        for _ in range(zero_count):
            nums.append(0)

        return nums
