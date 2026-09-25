class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxIdx = 0
        maxNum = nums[0]

        for i, num in enumerate(nums):
            if num > maxNum:
                maxIdx = i
                maxNum = num

        if any(num * 2 > maxNum for num in nums if num != maxNum):
            return -1

        return maxIdx
