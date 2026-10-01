class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def digitsSum(num: int) -> int:
            digitsSum = 0

            while num:
                digitsSum += num % 10
                num //= 10

            return digitsSum

        for i, num in enumerate(nums):
            if digitsSum(num) == i:
                return i

        return -1
