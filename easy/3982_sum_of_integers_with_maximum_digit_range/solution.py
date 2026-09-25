class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxDigitRange = 0
        maxDigitRangeSum = 0

        for num in nums:
            numCopy = num

            minDigit = 9
            maxDigit = 0

            while numCopy:
                digit = numCopy % 10
                minDigit = min(minDigit, digit)
                maxDigit = max(maxDigit, digit)

                numCopy //= 10

            digitRange = maxDigit - minDigit

            if digitRange > maxDigitRange:
                maxDigitRange = digitRange
                maxDigitRangeSum = num
            elif digitRange == maxDigitRange:
                maxDigitRangeSum += num

        return maxDigitRangeSum
