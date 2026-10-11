class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)

        sumOfSquares = 0

        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                sumOfSquares += num**2

        return sumOfSquares
