from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        blue = len(nums) - 1

        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]

                if i == red:
                    i += 1

                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:
                i += 1
