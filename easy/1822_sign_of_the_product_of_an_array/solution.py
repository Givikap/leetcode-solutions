from functools import reduce


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        nums_product = reduce(lambda x, y: x * y, nums)

        if nums_product > 0:
            return 1
        elif nums_product == 0:
            return 0
        else:
            return -1
