from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigit(num: int) -> int:
            digitCount = 0

            while num:
                digitCount += 1
                num //= 10

            return digitCount

        numCount = 0

        for num in nums:
            if countDigit(num) % 2 == 0:
                numCount += 1

        return numCount
