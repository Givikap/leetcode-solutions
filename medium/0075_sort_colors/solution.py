from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colorsCounts = [0] * 3

        for num in nums:
            colorsCounts[num] += 1

        color = 0
        for i in range(len(nums)):
            while not colorsCounts[color]:
                color += 1

            nums[i] = color
            colorsCounts[color] -= 1
