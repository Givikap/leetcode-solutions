class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        bitwise_array = [0] * len(nums)

        for i, num in enumerate(nums):
            if num & 1:
                bitwise_array[i] = num & ~(((num + 1) & ~num) >> 1)
            else:
                bitwise_array[i] = -1

        return bitwise_array
