class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        cumilative_xor = len(nums)

        for i, num in enumerate(nums):
            cumilative_xor ^= i ^ num

        return cumilative_xor
