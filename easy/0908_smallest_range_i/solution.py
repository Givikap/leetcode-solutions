class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        maxNum = minNum = nums[0]

        for num in nums:
            if num > maxNum:
                maxNum = num
            elif num < minNum:
                minNum = num

        return max(maxNum - minNum - 2 * k, 0)
