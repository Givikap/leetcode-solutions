class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        return [
            num
            for i in range(0, len(nums), 2)
            for num in [nums[i + 1]] * nums[i]
        ]
